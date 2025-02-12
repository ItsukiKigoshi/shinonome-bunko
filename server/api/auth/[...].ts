// file: ~/server/api/auth/[...].ts
import GithubProvider from 'next-auth/providers/github';
import { NuxtAuthHandler } from '#auth';
import { useRuntimeConfig } from '#imports';

export default NuxtAuthHandler({
  secret: useRuntimeConfig().authSecret,
  providers: [
    // @ts-expect-error Use .default here for it to work during SSR.
    GithubProvider.default({
      clientId: useRuntimeConfig().githubClientId,
      clientSecret: useRuntimeConfig().githubClientSecret
    })
  ]
});
