# React + TypeScript + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) (or [oxc](https://oxc.rs) when used in [rolldown-vite](https://vite.dev/guide/rolldown)) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend updating the configuration to enable type-aware lint rules:

```js
export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...

      // Remove tseslint.configs.recommended and replace with this
      tseslint.configs.recommendedTypeChecked,
      // Alternatively, use this for stricter rules
      tseslint.configs.strictTypeChecked,
      // Optionally, add this for stylistic rules
      tseslint.configs.stylisticTypeChecked,

      // Other configs...
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```

You can also install [eslint-plugin-react-x](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-x) and [eslint-plugin-react-dom](https://github.com/Rel1cx/eslint-react/tree/main/packages/plugins/eslint-plugin-react-dom) for React-specific lint rules:

```js
// eslint.config.js
import reactX from 'eslint-plugin-react-x'
import reactDom from 'eslint-plugin-react-dom'

export default defineConfig([
  globalIgnores(['dist']),
  {
    files: ['**/*.{ts,tsx}'],
    extends: [
      // Other configs...
      // Enable lint rules for React
      reactX.configs['recommended-typescript'],
      // Enable lint rules for React DOM
      reactDom.configs.recommended,
    ],
    languageOptions: {
      parserOptions: {
        project: ['./tsconfig.node.json', './tsconfig.app.json'],
        tsconfigRootDir: import.meta.dirname,
      },
      // other options...
    },
  },
])
```

## Cegid JFrog npm setup

To install `@cegid/*` packages, authenticate to the Cegid JFrog registry.

1) Get your token:
- Open https://cegid.jfrog.io/ui/user_profile
- Generate an Access Token (or use "Set Me Up" on the npm repo)

2) Login via npm (recommended):

```powershell
npm login --registry=https://cegid.jfrog.io/artifactory/api/npm/dsy-npm-all/ --scope=@cegid
```

- Username: your JFrog username
- Password: paste the generated token
- Email: your email

3) `.npmrc` options:
- Project-level config: see [frontend/.npmrc](frontend/.npmrc)
- User-level (safer): `%USERPROFILE%\.npmrc`

Example content:

```ini
@cegid:registry=https://cegid.jfrog.io/artifactory/api/npm/dsy-npm-all/
//cegid.jfrog.io/:_authToken=<your-token>
//cegid.jfrog.io/:email=ronaldo.drumond@cegid.com
//cegid.jfrog.io/:always-auth=true
```

4) Verify:

```powershell
npm ping --registry=https://cegid.jfrog.io/artifactory/api/npm/dsy-npm-all/
npm whoami --registry=https://cegid.jfrog.io/artifactory/api/npm/dsy-npm-all/
npm view @cegid/cds-react version --registry=https://cegid.jfrog.io/artifactory/api/npm/dsy-npm-all/
```

Security tip: prefer storing tokens in your user `.npmrc` to avoid committing secrets in the repo.
