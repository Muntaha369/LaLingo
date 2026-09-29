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
import ResponseView from "@/components/ResponseView";
import axios from "axios";

// async function sendPost(vid_aud:string, summary:string, language:string) {
//   try {
//     const response = await axios.post("http://localhost:8000/summaries", {
//       vid_aud: vid_aud,
//       summary: summary,
//       language: language
//     });

//     console.log("Status:", response.status);
//     console.log("Data:", response.data);
//   } catch (error) {
//     if (axios.isAxiosError(error)) {
//       if (error.response) {
//         console.error("Error:", error.response.status, error.response.data);
//       } else {
//         console.error("Request failed:", error.message);
//       }
//     } else {
//       console.error("Unexpected error:", error);
//     }
//   }
// }

const YT = /^(https?:\/\/)?(www\.|m\.)?(youtube\.com\/(watch\?v=|shorts\/|embed\/)|youtu\.be\/)[\w-]{6,}/i;

export default function Page() {
  const [url, setUrl] = useState("");
  const [language, setLanguage] = useState("");
  const [summarize, setSummarize] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [response, setResponse] = useState<string | null>(null);

  const process = useCallback(async () => {
    if (loading) return;
    if (!YT.test(url.trim())) {
      setError("Enter a valid YouTube URL");
      return;
    }
    setError(null);
    setLoading(true);
    try {
      const result = await axios.post("http://localhost:8000/summaries/", {
        vid_aud: url.trim(),
        summary:summarize,
        language,
      });
      // Assuming the backend returns { response: string }
      if (result.data && typeof result.data.response === "string") {
        setResponse(result.data.response);
      } else if (typeof result.data === "string") {
        setResponse(result.data);
      } else {
        setResponse(JSON.stringify(result.data, null, 2));
      }
    } catch (err) {
      if (axios.isAxiosError(err)) {
        if (err.response) {
          setError(`Error: ${err.response.status} ${err.response.data}`);
        } else {
          setError(`Error: ${err.message}`);
        }
      } else {
        setError("Unexpected error");
      }
    } finally {
      setLoading(false);
    }
  }, [url, language, summarize, loading]);

  const goBack = () => {
    setResponse(null);
    setUrl("");
    setLanguage("");
    setError(null);
  };

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key === "Enter") {
        e.preventDefault();
        if (response) {
          // In response view, Enter could trigger something else? We'll just ignore or maybe focus on question input later.
          // For now, do nothing.
        } else {
          process();
        }
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [process, response]);

  return (
    <main className="flex min-h-screen w-full flex-col items-center justify-center px-4 py-8 md:py-10 lg:pb-16">
      <div className="flex w-full max-w-[448px] flex-col md:max-w-[560px] lg:max-w-[680px]">
        <StatusBadge />
        <LogoHeader />
        <div className="mt-8 flex flex-col gap-5 md:mt-9 md:gap-6 lg:mt-12 lg:gap-7">
          {response ? (
            <>
              <ResponseView
                response={response}
                url={url}
                language={language}
                summarize={summarize}
                onGoBack={goBack}
              />
            </>
          ) : (
            <>
              <UrlInput value={url} onChange={(v) => { setUrl(v); setError(null); }} error={error} />
              <TranslateInput value={language} onChange={setLanguage} disabled={!summarize} />
              <LanguageSuggestions onSelect={setLanguage} disabled={!summarize} />
              <SummarizeCard checked={summarize} onChange={setSummarize} />
              <ProcessButton loading={loading} onClick={process} />
            </>
          )}
          <BottomStatusBar />
        </div>
      </div>
    </main>
  );
}
