prompts = [
    "Explain what machine learning is in 3 simple sentences.",
    "Give 3 real-world examples of artificial intelligence.",
    "Why is data cleaning important in AI?"
]

def fake_llm(prompt):
    # Simple rule-based responses to simulate an AI
    if "machine learning" in prompt.lower():
        return "Machine learning is when computers learn from data instead of being directly programmed. It finds patterns in data. Then it uses those patterns to make predictions."

    elif "examples" in prompt.lower() or "ai" in prompt.lower():
        return "AI is used in self-driving cars, recommendation systems like Netflix, and voice assistants like Siri."

    elif "data cleaning" in prompt.lower():
        return "Data cleaning is important because bad or messy data leads to incorrect results. Clean data helps models learn better and make accurate predictions."

    else:
        return "This is a simulated AI response."

# Run experiments
results = []

for i, prompt in enumerate(prompts, start=1):
    output = fake_llm(prompt)
    results.append((prompt, output))

    print("=" * 60)
    print(f"Experiment {i}")
    print(f"Input: {prompt}")
    print("Output:")
    print(output)
    print()

# Save results to a file
with open("results.txt", "w") as f:
    for i, (prompt, output) in enumerate(results, start=1):
        f.write("=" * 60 + "\n")
        f.write(f"Experiment {i}\n")
        f.write(f"Input: {prompt}\n")
        f.write("Output:\n")
        f.write(output + "\n\n")

print("Done. Results saved to results.txt")
