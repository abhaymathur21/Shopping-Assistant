class PaymentRequest(Model):
    wallet_address: str
    amount: int
    denom: str


# TransactionInfo will contain the identifier (tx_hash) for the transaction sent by the Payer agent.
class TransactionInfo(Model):
    tx_hash: str


# This message handler responsds to PaymentRequest messages by sending tokens from Payer's wallet address.
# Finally, it sends back the transaction hash for verification
@agent.on_message(model=PaymentRequest, replies=TransactionInfo)
async def send_payment(ctx: Context, sender: str, msg: PaymentRequest):
    ctx.logger.info(f"Received payment request from {sender}: {msg}")

    # send the payment
    transaction = ctx.ledger.send_tokens(
        msg.wallet_address, msg.amount, msg.denom, ctx.wallet
    ).wait_to_complete()

    # send the transaction hash so Payment Requester agent can confirm
    await ctx.send(sender, TransactionInfo(tx_hash=transaction.tx_hash))
    ctx.logger.info(f"Sending back TX: {transaction.tx_hash}")
