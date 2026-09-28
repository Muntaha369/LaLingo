import { ArrowRight, Loader2, Zap } from "lucide-react";

interface Props { loading: boolean; onClick: () => void }

export default function ProcessButton({ loading, onClick }: Props) {
  return (
    <button
      type="button"
      onClick={onClick}
      disabled={loading}
      className="flex h-[62px] md:h-[66px] lg:h-[72px] w-full items-center justify-center gap-3 rounded-xl bg-gradient-to-r from-cyan via-[#3a8fe0] to-royal text-[19px] font-medium text-[#0d1b3a] lg:text-[21px] disabled:opacity-80"
    >
      {loading ? <Loader2 className="h-5 w-5 animate-spin" /> : <Zap className="h-5 w-5" fill="currentColor" />}
      {loading ? "Processing…" : "Process Video"}
      {!loading && <ArrowRight className="h-5 w-5" />}
    </button>
  );
}
