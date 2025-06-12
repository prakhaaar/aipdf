import { useState } from "react";
import { askQuestion } from "../services/api";

export default function AskQuestion() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [docId, setDocId] = useState(""); // optional

  const handleAsk = async (e) => {
    e.preventDefault();
    const res = await askQuestion(question, docId);
    setAnswer(res?.answer || "No answer found.");
  };

  return (
    <div className="p-6">
      <h2 className="text-xl font-semibold mb-4">Ask a Question</h2>
      <form onSubmit={handleAsk} className="space-y-4">
        <input
          type="text"
          placeholder="Your question"
          className="border px-3 py-2 w-full"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          required
        />
        <button
          type="submit"
          className="bg-green-600 text-white px-4 py-2 rounded"
        >
          Ask
        </button>
      </form>
      {answer && (
        <div className="mt-6 text-lg text-blue-700">Answer: {answer}</div>
      )}
    </div>
  );
}
