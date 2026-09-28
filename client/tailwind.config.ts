import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        bg: "#0d0d0f",
        surface: "#19191c",
        line: "#26262b",
        cyan: "#4dd7f2",
        royal: "#3157d9",
        mint: "#5eead4",
        muted: "#9aa3b5",
        dim: "#6b7280",
      },
      fontFamily: {
        sans: ["var(--font-sans)", "system-ui", "sans-serif"],
        mono: ["var(--font-mono)", "ui-monospace", "monospace"],
      },
    },
  },
  plugins: [],
};
export default config;
