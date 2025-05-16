from langchain.prompts import PromptTemplate

COT_AGENT_INSTRUCTION = """Decide the operation of this round of the game by having a Thought, then Finish with your operation. Thought can reason about the current game status. Finish[operation] returns the operation and finishes the round. You will receive the game rules as well as your current game status.
Here are the rules:
{rules}
Here are some examples:
{examples}
(END OF EXAMPLES)
Game Status:
{status} 
Question: What is the operation?
{scratchpad}"""

cot_agent_prompt = PromptTemplate(
                        input_variables=["rules", "examples", "status", "scratchpad"],
                        template = COT_AGENT_INSTRUCTION,
                        )
