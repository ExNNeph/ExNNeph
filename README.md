### Hi, I'm Alex 👋

I build **LLM applications that are measured, not guessed**: every project comes with a labeled eval set,
guardrails that check the model's output before anyone sees it, tests, CI and a local demo.

- 🎓 M.Sc. Digital Business
- 📍 Frankfurt, Hesse, Germany
- 🔍 Open to **AI Engineer** roles

### Skills

<table>
  <tr>
    <th>Built with (in my public repos)</th>
    <th>Also worked with</th>
    <th>Learning now</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="https://skillicons.dev/icons?i=py,githubactions,git,github" /><br>
      <img src="https://img.shields.io/badge/Claude_API-D97757?style=for-the-badge&logo=anthropic&logoColor=white" />
      <img src="https://img.shields.io/badge/RAG_(BM25)-5A45FF?style=for-the-badge" />
      <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" />
      <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
      <img src="https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" />
    </td>
    <td valign="top">
      <img src="https://skillicons.dev/icons?i=vscode,obsidian,linux" /><br>
      <img src="https://img.shields.io/badge/OpenAI_API-412991?style=for-the-badge" />
      <img src="https://img.shields.io/badge/Gemini_API-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white" />
      <img src="https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white" />
      <img src="https://img.shields.io/badge/Slack_Apps-4A154B?style=for-the-badge" />
      <img src="https://img.shields.io/badge/VPS_·_Hostinger-673DE6?style=for-the-badge&logo=hostinger&logoColor=white" />
    </td>
    <td valign="top">
      <img src="https://skillicons.dev/icons?i=pytorch,fastapi,sqlite" /><br>
      <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" />
      <img src="https://img.shields.io/badge/LoRA_·_MLX-111111?style=for-the-badge" />
      <img src="https://img.shields.io/badge/Vector_search-00897B?style=for-the-badge" />
      <img src="https://img.shields.io/badge/Agents-6E40C9?style=for-the-badge" />
    </td>
  </tr>
</table>

### Projects

| Project | What it does | Technique | Measured result |
|---|---|---|---|
| [hybrid-rag](https://github.com/ExNNeph/hybrid-rag) | Answers questions over internal docs (DE/EN) with quotes checked against the sources | BM25 + local embeddings, RRF, cross-encoder rerank, semantic cache | recall@3 0.72 → 0.94, 38/40 correct, 0/14 false cache hits |
| [text-to-sql](https://github.com/ExNNeph/text-to-sql) | Plain-English questions to SQL on a shop database; only one read-only SELECT may run | structured outputs, sqlglot guardrails, read-only sandbox, confidence gate | 29/30 correct, 0 false blocks, 20/20 attacks harmless |
| [review-replier](https://github.com/ExNNeph/review-replier) | Replies to Google reviews in a business's own voice; serious cases go to a human | few-shot, calibrated LLM judge, escalation | voice score 3.9 → 4.8, escalation recall 100% |
| [listing-writer](https://github.com/ExNNeph/listing-writer) | Photo in, marketplace listing out (Vinted, eBay, Etsy; DE/EN) | vision, grounding guardrail | 0 invented brands in 36 listings |
| [contract-red-flags](https://github.com/ExNNeph/contract-red-flags) | Flags contract clauses worth asking about before you sign (DE/EN) | retrieval (BM25) over a risk knowledge base | 0 of 27 fair clauses wrongly flagged |
| [meeting-tasks](https://github.com/ExNNeph/meeting-tasks) | Meeting notes → GitHub Issues, only with tasks that are really in the notes | structured outputs, quote guardrail | 100% precision / 98% recall on the hard set |
| [invoice-chaser](https://github.com/ExNNeph/invoice-chaser) | Polite, escalating payment reminders for freelancers | guardrail + self-correcting retry | 100% of drafts pass the checks |

Each README has screenshots, a step-by-step guide to run it locally, the eval results and their limits.

### Currently building

- [x] **[Text-to-SQL with guardrails](https://github.com/ExNNeph/text-to-sql)**: destructive or unsafe queries are blocked before they run
- [x] **[Hybrid RAG with citations](https://github.com/ExNNeph/hybrid-rag)**: BM25 + embeddings, reranking, every claim checked against its source, plus a semantic cache
- [ ] **Agent system**: tools, memory and a human-in-the-loop checkpoint for risky actions
- [ ] **LoRA fine-tuning**: a small local model trained on my eval data, benchmarked against the base model and Claude

### Recent activity

<!--START_SECTION:activity-->
- 🎉 Published [review-replier](https://github.com/ExNNeph/review-replier) · 2026-10-26
- 🎉 Published [listing-writer](https://github.com/ExNNeph/listing-writer) · 2026-10-25
- 🎉 Published [contract-red-flags](https://github.com/ExNNeph/contract-red-flags) · 2026-10-25
- 🎉 Published [meeting-tasks](https://github.com/ExNNeph/meeting-tasks) · 2026-10-25
- ⬆️ Pushed to [invoice-chaser](https://github.com/ExNNeph/invoice-chaser) · 2026-10-25
<!--END_SECTION:activity-->

### Contributions

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/ExNNeph/ExNNeph/output/snake-dark.svg" />
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/ExNNeph/ExNNeph/output/snake.svg" />
</picture>

### Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alexander-kramer-0b242320b)
