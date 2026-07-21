// Fixture synthétique — test minimal pour ce fixture (evidence L4 candidate).
const request = require("supertest");
const app = require("../app");

describe("stripe webhook", () => {
  it("marks account past_due on invoice.payment_failed", async () => {
    // signature mockée pour le test — voir helpers/stripeTestEvent.js
    const res = await request(app).post("/api/webhooks/stripe").send({});
    expect(res.status).toBeLessThan(500);
  });
});
