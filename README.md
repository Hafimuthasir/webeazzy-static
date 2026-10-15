# Webeazzy — www.webeazzy.com

Static site for Webeazzy, a cloud platform. Deployed on Vercel from this repository.

## Pages

- `index.html` — the platform homepage: products (Strada, Begone, Device Cloud), why Webeazzy,
  getting started, FAQ and a contact form.
- `background-remover.html` — the Begone (AI background removal) product page. It talks to the
  live Begone service (`begone-gateway.webeazzy.com`, `begone.webeazzy.com`); change it only together
  with the Begone team.
- `privacy.html`, `terms.html` — the Privacy Policy and Terms of Service, served at `/privacy` and
  `/terms`. They share `legal.css`. Keep them limited to commitments the business has actually made.
- `og-image.png` — the 1200×630 social preview image used by every page.
- `llms.txt` — a plain-text summary of Webeazzy and its products for AI assistants.

## Products linked from the site

| Product | Status | Where |
| --- | --- | --- |
| Strada — backend as a service | Live | https://strada.webeazzy.com (docs at `/docs`) |
| Begone — AI background removal | Live | `/background-remover`, https://begone.webeazzy.com |
| Device Cloud — connected device management | Live | `/#device-cloud`, "Get started" through the contact form |

Strada and Begone have free trials. Pricing is not shown yet, except Begone's published per-image price.
Internal links use clean URLs (`/background-remover`, `/privacy`), since `cleanUrls` redirects `.html` paths.

## Contact form

The "Talk to us" and waitlist buttons open one form. Submissions are stored in the visitor's
browser and posted to `/api/webeazzy/leads`, which `vercel.json` forwards to the existing lead
inbox at `platform.webeazzy.com`. The label says what the visitor asked for (for example
`Cloud: Device Cloud: get started`).

## Theme

Inter, a purple primary (`--purple-600: #7F56D9`) and the light card style in the `<style>` block
of `index.html`. Keep new sections on the same tokens.
