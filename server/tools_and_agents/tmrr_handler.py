from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
from openrouter.errors import TooManyRequestsResponseError
import httpx

@retry(
    retry=retry_if_exception_type((TooManyRequestsResponseError, httpx.HTTPStatusError)),
    wait=wait_exponential(multiplier=2, min=4, max=60),
    stop=stop_after_attempt(5),
    reraise=True
)
def invoke_agent_with_retry(agent, payload):
    return agent.invoke(payload)