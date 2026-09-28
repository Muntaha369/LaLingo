import { Globe, Languages } from "lucide-react";

interface Props { value: string; onChange: (v: string) => void }

export default function TranslateInput({ value, onChange }: Props) {
  return (
    <section>
      <div className="flex items-center justify-between px-[2px]">
        <label htmlFor="lang" className="flex items-center gap-2 font-mono text-[14px] font-medium lg:text-[15px] text-white">
          <Languages className="h-4 w-4 text-cyan" /> Translate
        </label>
        <span className="font-mono text-[12px] lg:text-[13px] text-muted">Auto-detecting src</span>
      </div>
      <div className="mt-3 flex h-[52px] md:h-[56px] lg:h-[60px] items-center rounded-xl border border-line bg-surface px-4 lg:px-5">
        <input
          id="lang"
          value={value}
          onChange={(e) => onChange(e.target.value)}
          placeholder="e.g. Hindi, German, Japanese"
          className="w-full bg-transparent text-[15px] text-white outline-none lg:text-[16px] placeholder:text-dim"
        />
        <Globe className="h-5 w-5 shrink-0 text-dim" />
      </div>
    </section>
  );
}
