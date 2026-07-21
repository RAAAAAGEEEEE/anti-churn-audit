# Fixture synthétique — code original écrit pour cet eval, aucune source tierce.
from flask import Blueprint, request, jsonify
from .db import accounts

paddle_webhooks = Blueprint("paddle_webhooks", __name__)


@paddle_webhooks.route("/api/webhooks/paddle", methods=["POST"])
def handle_paddle_webhook():
    event = request.get_json()
    event_type = event.get("event_type")

    if event_type == "subscription.past_due":
        accounts.mark_past_due(event["data"]["customer_id"])
    elif event_type == "subscription.canceled":
        accounts.revoke_entitlements(event["data"]["customer_id"])
    elif event_type == "transaction.completed":
        # Paiement recu (y compris apres recuperation par Paddle) :
        # on restaure les droits au cas ou le compte etait past_due.
        accounts.restore_entitlements(event["data"]["customer_id"])
        accounts.clear_past_due(event["data"]["customer_id"])

    return jsonify({"received": True})
