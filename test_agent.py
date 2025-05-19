import os
import requests
from agent import build_graph
from langchain_core.messages import HumanMessage

class BasicAgent:
    def __init__(self):
        print("Initializing BasicAgent...")
        self.graph = build_graph()

    def __call__(self, question: str) -> str:
        print(f"\nProcessing question: {question}")
        messages = [HumanMessage(content=question)]
        messages = self.graph.invoke({"messages": messages})
        answer = messages['messages'][-1].content
        return answer[14:]  # Remove the "Answer: " prefix

def test_agent(max_questions):
    # Get questions from the API
    api_url = "https://agents-course-unit4-scoring.hf.space"
    questions_url = f"{api_url}/questions"
    
    print(f"Fetching questions from: {questions_url}")
    try:
        response = requests.get(questions_url, timeout=15)
        response.raise_for_status()
        questions_data = response.json()
        if not questions_data:
            print("No questions received from the API")
            return
 
        questions_data = questions_data[:max_questions]
        print(f"\n{'='*80}")
        print(f"Processing {len(questions_data)} out of {len(questions_data)} questions (limited to {max_questions})")
        print("="*80)
        
        # Initialize agent
        agent = BasicAgent()
        
        # Process each question
        results = []
        for item in questions_data:
            task_id = item.get("task_id")
            question = item.get("question")
            
            if not task_id or question is None:
                print(f"Skipping invalid question: {item}")
                continue
                
            print(f"\n{'='*80}")
            print(f"TASK ID: {task_id}")
            print(f"QUESTION: {question}")
            
            try:
                answer = agent(question)
                print(f"ANSWER: {answer}")
                results.append({
                    "task_id": task_id,
                    "question": question,
                    "answer": answer
                })
            except Exception as e:
                print(f"ERROR processing question: {e}")
                results.append({
                    "task_id": task_id,
                    "question": question,
                    "error": str(e)
                })
        
        # Save results to a file
        import json
        with open('agent_results.json', 'w') as f:
            json.dump(results, f, indent=2)
            
        print("\n" + "="*80)
        print(f"Processing complete. Results saved to agent_results.json")
        
    except Exception as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    test_agent(max_questions=3) 