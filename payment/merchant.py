class PaymentRequest(Model):
    wallet_address: str
    amount: int
    denom: str


# TransactionInfo will contain the tx_hash of the payment response transaction that will be sent by the Payer agent
class TransactionInfo(Model):
    tx_hash: str


AMOUNT = 100
DENOM = "atestfet"

customer_address = "agent1qtdzkr0nwjpnulzsvw0h22nh4hp8rnpmgzaxp7vmmll0t88q5l6v6wqewa2"


# This interval task sends a PaymentRequest to Payer agent every 10 seconds.
# It includes the Payment Requester agent wallet address, AMOUNT and DENOM.
@agent.on_interval(period=10.0)
async def request_funds(ctx: Context):
    await ctx.send(
        customer_address,
        PaymentRequest(
            wallet_address=str(ctx.wallet.address()), amount=AMOUNT, denom=DENOM
        ),
    )


# The message handler below is activated when a TransactionInfo message is received
# It first loops until the transaction is completed and then querys the transaction
# information to confirm that it was successful.
@agent.on_message(model=TransactionInfo)
async def confirm_transaction(ctx: Context, sender: str, msg: TransactionInfo):
    ctx.logger.info(f"Received transaction info from {sender}: {msg}")

    try:
        tx_resp = ctx.ledger.query_tx(msg.tx_hash)
        coin_received = tx_resp.events["coin_received"]

        # verify that transaction was successful
        if (
            coin_received["receiver"] == str(ctx.wallet.address())
            and coin_received["amount"] == f"{AMOUNT}{DENOM}"
        ):
            ctx.logger.info(
                f"Transaction {msg.tx_hash} was successful: {coin_received}"
            )

        else:
            ctx.logger.info(f"Transaction {msg.tx_hash} was NOT successful")

    except:
        ctx.logger.info(
            f"There was an error while attempting to confirm the transaction."
        )
