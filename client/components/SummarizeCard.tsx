import { Check } from "lucide-react";

interface Props { checked: boolean; onChange: (v: boolean) => void }

export default function SummarizeCard({ checked, onChange }: Props) {
  return (
    <label className="flex cursor-pointer items-start gap-3 rounded-xl border border-line bg-surface px-4 py-3.5 lg:gap-4 lg:px-6 lg:py-5">
      <input type="checkbox" checked={checked} onChange={(e) => onChange(e.target.checked)} className="peer sr-only" />
      <span className="mt-0.5 flex h-6 w-6 shrink-0 items-center justify-center rounded-md border-2 border-line bg-transparent text-transparent peer-checked:border-cyan peer-checked:bg-cyan peer-checked:text-white">
        <Check className="h-4 w-4" strokeWidth={3} />
      </span>
      <span className="flex-1">
        <span className="flex items-center justify-between">
          <span className="text-[19px] font-medium leading-6 lg:text-[21px] text-white">Summarize</span>
          <span className="font-mono text-[12px] text-mint lg:text-[13px]">Digest Mode</span>
        </span>
        <span className="mt-1 block text-[14px] leading-5 lg:mt-1.5 lg:text-[15px] lg:leading-6 text-muted">
          Extract executive takeaways, structured outline, and key timestamps directly from the audio stream.
        </span>
      </span>
    </label>
  );
}
