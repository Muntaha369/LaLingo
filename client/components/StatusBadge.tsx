export default function StatusBadge() {
  return (
    <div className="flex justify-center">
      <div className="flex h-[22px] items-center gap-2 rounded-full bg-surface px-3 font-mono text-[12px] leading-none">
        <span className="h-2 w-2 rounded-full bg-emerald-400" />
        <span className="font-medium uppercase tracking-wide text-emerald-400">Model V2.4 Active</span>
        <span className="text-dim">/</span>
        <span className="text-muted">42ms latency</span>
      </div>
    </div>
  );
}
