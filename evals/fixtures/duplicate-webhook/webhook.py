# Fixture synthétique — code original écrit pour cet eval, aucune source tierce.
from flask import Blueprint, request, jsonify
from .db import accounts

lemonsqueezy_webhooks = Blueprint("lemonsqueezy_webhooks", __name__)


@lemonsqueezy_webhooks.route("/api/webhooks/lemonsqueezy", methods=["POST"])
def handle_webhook():
    payload = request.get_json()
    event_name = payload.get("meta", {}).get("event_name")
    customer_id = payload.get("data", {}).get("attributes", {}).get("customer_id")

    # Pas de vérification d'event_id : si Lemon Squeezy livre deux fois
    # le même événement (retry réseau, timeout), ce handler l'appliquera
    # deux fois sans détection.
    if event_name == "subscription_payment_failed":
        accounts.mark_past_due(customer_id)
    elif event_name == "subscription_payment_recovered":
        accounts.restore_entitlements(customer_id)
        accounts.clear_past_due(customer_id)

    return jsonify({"received": True})
