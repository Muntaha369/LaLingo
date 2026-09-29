import { ArrowLeft, Info, Video } from "lucide-react";

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
  return (
    <div className="space-y-6">
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
    </div>
  );
}