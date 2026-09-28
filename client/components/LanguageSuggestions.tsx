const LANGS = ["Spanish", "Japanese", "German", "Hindi"];

export default function LanguageSuggestions({ onSelect, disabled = false }: { onSelect: (l: string) => void; disabled?: boolean }) {
  return (
    <div className={disabled ? "opacity-75 pointer-events-none" : "-mt-1 flex flex-wrap items-center gap-2 font-mono text-[12px] lg:gap-2.5 lg:text-[13px] text-muted"}>
      <span className={disabled ? "text-muted" : "mr-0.5"}>Suggestions:</span>
      {LANGS.map((l) => (
        <button
          key={l}
          type="button"
          onClick={() => !disabled && onSelect(l)}
          className={`rounded-full bg-surface px-3 py-1 text-white lg:px-3.5 lg:py-1.5 transition-colors hover:bg-line ${disabled ? "cursor-not-allowed opacity-75" : ""}`}
          disabled={disabled}
        >
          {l}
        </button>
      ))}
    </div>
  );
}
