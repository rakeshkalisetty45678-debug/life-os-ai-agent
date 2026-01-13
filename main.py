from context import analyze_context
from memory import fetch_memory
from decision import decision_engine
from llm import ask_llm
from actions import build_action_plan

user_input = input("Cheppu ra, em problem? ")

context = analyze_context(user_input)
memory = fetch_memory(context)
decision = decision_engine(context, memory)
llm_output = ask_llm(user_input, context, decision)
final_answer = build_action_plan(llm_output)

print("\n🤖 LIFE OS AI OUTPUT:\n")
print(final_answer)
