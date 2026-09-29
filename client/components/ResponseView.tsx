import { ArrowLeft, ArrowRight, Info, Loader2, Video } from "lucide-react";
import { useState } from "react";
import axios from "axios";

interface Props {
  response: string;
  url: string;
  language: string;
  summarize: boolean;
  onGoBack: () => void;
}

export default function ResponseView({
  response,
  url,
  language,
  summarize,
  onGoBack,
}: Props) {
  const [query, setQuery] = useState("");
  const [followUpHistory, setFollowUpHistory] = useState<Array<{ question: string; answer: string }>>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleAsk = async () => {
    const trimmed = query.trim();
    if (!trimmed || loading) return;
    setError(null);
    setLoading(true);
    try {
      const result = await axios.post("http://localhost:8000/ask", {
        query: trimmed,
      });
      let answerText = "";
      if (typeof result.data === "string") {
        answerText = result.data;
      } else if (result.data && typeof result.data.response === "string") {
        answerText = result.data.response;
      } else if (result.data && typeof result.data.answer === "string") {
        answerText = result.data.answer;
      } else if (result.data && typeof result.data.result === "string") {
        answerText = result.data.result;
      } else {
        answerText = JSON.stringify(result.data, null, 2);
      }
      setFollowUpHistory((prev) => [...prev, { question: trimmed, answer: answerText }]);
      setQuery("");
    } catch (err) {
      setError("Unable to get a response. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6 pb-16">
      {/* Header with back button and info */}
      <div className="flex items-center justify-between flex-wrap gap-3">
        <div className="flex items-center gap-2">
          <button
            onClick={onGoBack}
            className="flex items-center gap-1.5 text-sm font-mono text-muted hover:text-white transition-colors"
          >
            <ArrowLeft className="h-4 w-4" /> Back to Input
          </button>
        </div>
        <div className="flex items-center gap-4 text-xs font-mono text-muted">
          <div className="flex items-center gap-1">
            <Info className="h-3 w-3" />
            <span>{summarize ? "Digest Mode" : "Translation Mode"}</span>
          </div>
          <div className="flex items-center gap-1">
            <Video className="h-3 w-3" />
            <span className="truncate max-w-[200px]">{url}</span>
          </div>
        </div>
      </div>

      {/* Response text area */}
      <div className="border border-line rounded-xl bg-surface p-4">
        <div className="whitespace-pre-wrap text-[15px] lg:text-[16px] leading-6 text-white max-h-[60vh] overflow-y-auto">
          {response}
        </div>
      </div>

      {/* Chronological follow-up history */}
      {followUpHistory.map((item, index) => (
        <div key={index} className="space-y-3">
          <div className="font-mono text-xs text-muted flex items-center gap-1.5 px-1">
            <span className="text-cyan font-semibold">Q:</span> {item.question}
          </div>
          <div className="border border-line rounded-xl bg-surface p-4">
            <div className="whitespace-pre-wrap text-[15px] lg:text-[16px] leading-6 text-white max-h-[60vh] overflow-y-auto">
              {item.answer}
            </div>
          </div>
        </div>
      ))}

      {/* Follow-up input section */}
      <div className="space-y-1.5">
        <div className={`flex h-[52px] md:h-[56px] lg:h-[60px] items-center rounded-xl border bg-surface px-4 lg:px-5 ${error ? "border-red-500/60" : "border-line"}`}>
          <input
            value={query}
            onChange={(e) => {
              setQuery(e.target.value);
              setError(null);
            }}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                e.preventDefault();
                handleAsk();
              }
            }}
            placeholder="Ask a follow-up question about this video..."
            disabled={loading}
            className="w-full bg-transparent text-[15px] text-white outline-none lg:text-[16px] placeholder:text-dim disabled:opacity-75"
          />
          <button
            type="button"
            onClick={handleAsk}
            disabled={loading || !query.trim()}
            className="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-cyan/10 text-cyan hover:bg-cyan/20 transition-colors disabled:opacity-40 disabled:pointer-events-none"
            title="Submit question"
          >
            {loading ? <Loader2 className="h-4 w-4 animate-spin" /> : <ArrowRight className="h-4 w-4" />}
          </button>
        </div>
        {error && (
          <p className="font-mono text-[12px] lg:text-[13px] text-red-400 px-1">
            {error}
          </p>
        )}
      </div>
    </div>
  );
}