"""Minimal JSON Schema (draft-07 subset) validator, stdlib-only.

Not a general-purpose implementation: it supports exactly the constructs
used by schemas/*.schema.json in this repo (type, enum, const, required,
properties, additionalProperties, items, local $ref, pattern, minimum,
maximum, minLength, maxLength, format=date-time). This is intentional —
adding a third-party dependency (e.g. `jsonschema`) for two validation
scripts would be a heavier dependency footprint than this project needs.
"""

from __future__ import annotations

import re
from datetime import datetime
from typing import Any


class SchemaError(Exception):
    def __init__(self, path: str, message: str):
        self.path = path
        self.message = message
        super().__init__(f"{path}: {message}")


def _resolve_ref(ref: str, root: dict) -> dict:
    if not ref.startswith("#/"):
        raise SchemaError(ref, f"unsupported $ref target: {ref}")
    node: Any = root
    for part in ref[2:].split("/"):
        if part not in node:
            raise SchemaError(ref, f"broken $ref, missing key {part!r}")
        node = node[part]
    return node


def _check_type(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "null":
        return value is None
    raise SchemaError("<type>", f"unknown type {expected!r} in schema")


def validate(instance: Any, schema: dict, root: dict | None = None, path: str = "$") -> list[str]:
    """Return a list of human-readable error strings (empty if valid)."""
    root = root if root is not None else schema
    errors: list[str] = []

    if "$ref" in schema:
        try:
            resolved = _resolve_ref(schema["$ref"], root)
        except SchemaError as exc:
            return [f"{path}: {exc.message}"]
        return validate(instance, resolved, root, path)

    if "const" in schema:
        if instance != schema["const"]:
            errors.append(f"{path}: expected const {schema['const']!r}, got {instance!r}")
        return errors

    if "enum" in schema:
        if instance not in schema["enum"]:
            errors.append(f"{path}: {instance!r} not in enum {schema['enum']!r}")
        return errors

    schema_type = schema.get("type")
    if schema_type is not None:
        types = schema_type if isinstance(schema_type, list) else [schema_type]
        if not any(_check_type(instance, t) for t in types):
            errors.append(f"{path}: expected type {schema_type!r}, got {type(instance).__name__}")
            return errors

    if isinstance(instance, str):
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            errors.append(f"{path}: {instance!r} does not match pattern {schema['pattern']!r}")
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errors.append(f"{path}: string shorter than minLength {schema['minLength']}")
        if "maxLength" in schema and len(instance) > schema["maxLength"]:
            errors.append(f"{path}: string longer than maxLength {schema['maxLength']}")
        if schema.get("format") == "date-time":
            try:
                datetime.fromisoformat(instance.replace("Z", "+00:00"))
            except ValueError:
                errors.append(f"{path}: {instance!r} is not a valid ISO-8601 date-time")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(f"{path}: {instance} < minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            errors.append(f"{path}: {instance} > maximum {schema['maximum']}")

    if isinstance(instance, list) and "items" in schema:
        for i, item in enumerate(instance):
            errors.extend(validate(item, schema["items"], root, f"{path}[{i}]"))

    if isinstance(instance, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                errors.append(f"{path}: missing required property {key!r}")

        properties = schema.get("properties", {})
        for key, value in instance.items():
            if key in properties:
                errors.extend(validate(value, properties[key], root, f"{path}.{key}"))
            elif schema.get("additionalProperties") is False:
                errors.append(f"{path}: additional property {key!r} not allowed")

    return errors


def validate_file(instance: Any, schema: dict) -> list[str]:
    return validate(instance, schema, schema, "$")
