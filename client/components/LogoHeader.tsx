import { Sparkles } from "lucide-react";

export default function LogoHeader() {
  return (
    <header className="mt-5 text-center lg:mt-7">
      <h1 className="relative inline-block text-[38px] font-bold leading-[44px] md:text-[44px] md:leading-[50px] lg:text-[52px] lg:leading-[58px] tracking-tight">
        <span className="bg-gradient-to-r from-white via-cyan to-royal bg-clip-text text-transparent">LaLingo</span>
        <Sparkles className="absolute -right-5 -top-1 h-4 w-4 lg:-right-6 lg:h-5 lg:w-5 text-cyan" />
      </h1>
      <p className="mt-3 text-[15px] leading-5 lg:mt-4 lg:text-[17px] lg:leading-6 text-muted">Translate and summarize videos with AI</p>
    </header>
  );
}
