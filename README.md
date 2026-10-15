# Webeazzy — www.webeazzy.com

Static site for Webeazzy, a cloud platform. Deployed on Vercel from this repository.

## Pages

- `index.html` — the platform homepage: products (Strada, Begone, Device Cloud), why Webeazzy,
  getting started, FAQ and a contact form.
- `background-remover.html` — the Begone (AI background removal) product page. It talks to the
  live Begone service (`begone-gateway.webeazzy.com`, `begone.webeazzy.com`); change it only together
  with the Begone team.

## Products linked from the site

| Product | Status | Where |
| --- | --- | --- |
| Strada — backend as a service | Live | https://strada.webeazzy.com (docs at `/docs`) |
| Begone — AI background removal | Live | `/background-remover`, https://begone.webeazzy.com |
| Device Cloud — connected device management | Coming soon | waitlist through the contact form |

Pricing is not shown yet, except Begone's published per-image price.

## Contact form

The "Talk to us" and waitlist buttons open one form. Submissions are stored in the visitor's
browser and posted to `/api/webeazzy/leads`, which `vercel.json` forwards to the existing lead
inbox at `platform.webeazzy.com`. The label says what the visitor asked for (for example
`Cloud: Device Cloud waitlist`).

## Theme

Inter, a purple primary (`--purple-600: #7F56D9`) and the light card style in the `<style>` block
of `index.html`. Keep new sections on the same tokens.
