import { useState, useEffect, useCallback } from "react";
import debounce from "lodash.debounce";

export function useSuggestion(value: string, systemPrompt: string) {
  const [suggestion, setSuggestion] = useState("");

  const debouncedGetSuggestion = useCallback(
    debounce(async (prompt: string, system_prompt: string, setter) => {
      try {
        const response = await fetch(
          import.meta.env.BASE_URL + "../api/suggestion",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              prompt: prompt,
              system_prompt: system_prompt,
            }),
          },
        );
        if (!response.ok) {
          throw new Error(response.statusText);
        }
        const data = await response.json();
        setter(data.suggestion);
      } catch (error) {
        console.error("Failed to fetch suggestion:", error);
      }
    }, 1000),
    [],
  );

  useEffect(() => {
    if (value) {
      debouncedGetSuggestion(value, systemPrompt, setSuggestion);
    }
  }, [value, systemPrompt, debouncedGetSuggestion]);

  return suggestion;
}
