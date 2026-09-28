"use client";

import { useCallback, useEffect, useState } from "react";
import StatusBadge from "@/components/StatusBadge";
import LogoHeader from "@/components/LogoHeader";
import UrlInput from "@/components/UrlInput";
import TranslateInput from "@/components/TranslateInput";
import LanguageSuggestions from "@/components/LanguageSuggestions";
import SummarizeCard from "@/components/SummarizeCard";
import ProcessButton from "@/components/ProcessButton";
import BottomStatusBar from "@/components/BottomStatusBar";
import axios from "axios";

async function sendPost() {
  try {
    const response = await axios.post("http://localhost:8000/ask", {
      query: "Muntaha",
    });

    console.log("Status:", response.status);
    console.log("Data:", response.data);
  } catch (error) {
    if (axios.isAxiosError(error)) {
      if (error.response) {
        console.error("Error:", error.response.status, error.response.data);
      } else {
        console.error("Request failed:", error.message);
      }
    } else {
      console.error("Unexpected error:", error);
    }
  }
}

const YT = /^(https?:\/\/)?(www\.|m\.)?(youtube\.com\/(watch\?v=|shorts\/|embed\/)|youtu\.be\/)[\w-]{6,}/i;

export default function Page() {
  const [url, setUrl] = useState("");
  const [language, setLanguage] = useState("");
  const [summarize, setSummarize] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const process = useCallback(async () => {
    if (loading) return;
    if (!YT.test(url.trim())) {
      setError("Enter a valid YouTube URL");
      return;
    }
    setError(null);
    setLoading(true);
    try {
      // TODO: replace with your real endpoint
      await new Promise((r) => setTimeout(r, 1800));
    } finally {
      setLoading(false);
    }
  }, [url, loading]);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === "Enter") {
        e.preventDefault();
        process();
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [process]);

  return (
    <main className="flex min-h-screen w-full flex-col items-center justify-center px-4 py-8 md:py-10 lg:pb-16">
      <div className="flex w-full max-w-[448px] flex-col md:max-w-[560px] lg:max-w-[680px]">
        <StatusBadge />
        <LogoHeader />
        <div className="mt-8 flex flex-col gap-5 md:mt-9 md:gap-6 lg:mt-12 lg:gap-7">
          <UrlInput value={url} onChange={(v) => { setUrl(v); setError(null); }} error={error} />
          <TranslateInput value={language} onChange={setLanguage} disabled={!summarize} />
          <LanguageSuggestions onSelect={setLanguage} disabled={!summarize} />
          <SummarizeCard checked={summarize} onChange={setSummarize} />
          <ProcessButton loading={loading} onClick={process} />
          <BottomStatusBar />
        </div>
      </div>
    </main>
  );
}
