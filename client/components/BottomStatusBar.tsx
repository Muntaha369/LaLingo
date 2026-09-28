import { Command, ShieldCheck } from "lucide-react";

export default function BottomStatusBar() {
  return (
    <footer className="flex items-center justify-between px-[2px] font-mono text-[12px] lg:text-[13px] text-muted">
      <span className="flex items-center gap-2">
        <Command className="h-3.5 w-3.5" /> Press <b className="font-semibold text-white">⌘ + Enter</b>
      </span>
      <span className="flex items-center gap-2">
        <ShieldCheck className="h-3.5 w-3.5 text-cyan" /> Zero Retention
      </span>
    </footer>
  );
}
