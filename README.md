# shinonome-bunko / 東雲文庫

やがて夜は明ける．

## In my mind...🤔

```mermaid
graph TD
    A["Images of Books (ex. 国立国会図書館デジタルコレクション)"] -->|OCR| B
    B["Text File (MD? XML?; UTF-8? Shift-JIS?)"] -->|"Parser? (Should I do this?)"| C
    B --> |"Iterate + Modify by Human (Editor in Browser or Git; cf. Wiki, Qiita, Zenn)"| B
    C["Aozora Bunko File Format?"] -->| | D
    D["Publish to Aozora Bunko?"]
```

1. Use Existing Aozora Bunko Files as Training Data
   - We can find original texts since Aozora Bunko shows the original version of the texts ("底本").
   - Supervised learning with these data

## This Project consists of...

1. Text Recognition
   - OCR with Python
   - Aim to generate texts accurately and quickly also in Japanese vertical texts
1. Viewer/Editor
   - Simple and Fast Viewer and Editor working on Browser
   - Anyone can modify the generated texts either in the Built-in Editor or GitHub (Can we compare the original pictures and the generated texts?)
   - Can this editor be built with Python as well?
1. Text Matching Game
   - Matching Game for Japanese Texts
   - Aim to improve the accuracy of OCR (also for fun, of course!)
   - This game can be a learning material for Japanese learners (like [the original concept of Duolingo](https://www.ted.com/talks/luis_von_ahn_massive_scale_online_collaboration))
   - cf. Google Captcha

## Related Projects

- [aozorahack](https://github.com/aozorahack)
  - [Web Page](https://aozorahack.org)
  - [ideathon](https://github.com/aozorahack/ideathon): There are many ideas similar to this project!
  - [kosakuin](https://github.com/aozorahack/kosakuin): Aozora Bunko Editor (MIT License)
  - [aozora-cli](https://github.com/aozorahack/aozora-cli): Aozora Bunko CLI (MIT License)
  - [aozora-parser.js](https://github.com/aozorahack/aozora-parser.js)
  - [aozoraflow](https://github.com/aozorahack/aozoraflow)
- [kyukyunyorituryo/AozoraEditor: 青空文庫エディタ](https://github.com/kyukyunyorituryo/AozoraEditor)
- [kyukyunyorituryo/html2aozora](https://github.com/kyukyunyorituryo/html2aozora)
- [gearsns/AozoraJavaScriptParser](https://github.com/gearsns/AozoraJavaScriptParser)

---

# Nuxt Minimal Starter

Look at the [Nuxt documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

## Setup

Make sure to install dependencies:

```bash
# npm
npm install

# pnpm
pnpm install

# yarn
yarn install

# bun
bun install
```

## Development Server

Start the development server on `http://localhost:3000`:

```bash
# npm
npm run dev

# pnpm
pnpm dev

# yarn
yarn dev

# bun
bun run dev
```

## Production

Build the application for production:

```bash
# npm
npm run build

# pnpm
pnpm build

# yarn
yarn build

# bun
bun run build
```

Locally preview production build:

```bash
# npm
npm run preview

# pnpm
pnpm preview

# yarn
yarn preview

# bun
bun run preview
```

Check out the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.
