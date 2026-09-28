const LANGS = ["Spanish", "Japanese", "German", "Hindi"];

export default function LanguageSuggestions({ onSelect }: { onSelect: (l: string) => void }) {
  return (
    <div className="-mt-1 flex flex-wrap items-center gap-2 font-mono text-[12px] lg:gap-2.5 lg:text-[13px] text-muted">
      <span className="mr-0.5">Suggestions:</span>
      {LANGS.map((l) => (
        <button
          key={l}
          type="button"
          onClick={() => onSelect(l)}
          className="rounded-full bg-surface px-3 py-1 text-white lg:px-3.5 lg:py-1.5 transition-colors hover:bg-line"
        >
          {l}
        </button>
      ))}
    </div>
  );
}
