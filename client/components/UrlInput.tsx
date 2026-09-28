import { Link2, SquarePlay } from "lucide-react";

interface Props { value: string; onChange: (v: string) => void; error: string | null }

export default function UrlInput({ value, onChange, error }: Props) {
  return (
    <section>
      <div className="flex items-center justify-between px-[2px]">
        <label htmlFor="url" className="flex items-center gap-2 font-mono text-[14px] font-medium lg:text-[15px] text-white">
          <Link2 className="h-4 w-4 text-cyan" /> YouTube URL
        </label>
        <span className="rounded bg-surface px-2 py-[3px] font-mono text-[12px] lg:text-[13px] text-muted">⌘V to paste</span>
      </div>
      <div className={`mt-3 flex h-[52px] md:h-[56px] lg:h-[60px] items-center rounded-xl border bg-surface px-4 lg:px-5 ${error ? "border-red-500/60" : "border-line"}`}>
        <input
          id="url"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder="https://youtube.com/watch?v=..."
          className="w-full bg-transparent text-[15px] text-white outline-none lg:text-[16px] placeholder:text-dim"
        />
        <SquarePlay className="h-5 w-5 shrink-0 text-dim" />
      </div>
      {error && <p className="mt-1.5 font-mono text-[12px] lg:text-[13px] text-red-400">{error}</p>}
    </section>
  );
}
