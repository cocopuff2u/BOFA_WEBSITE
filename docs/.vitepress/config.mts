import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/',
  title: "BOFA",
  description: "Browser Overview Feed for Apple",
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'BOFA - Browser Overview Feed for Apple' }],
    ['meta', { property: 'og:description', content: 'Empowering Mac administrators with up-to-date browser version information for Apple devices' }],
    ['meta', { property: 'og:image', content: 'https://mofa.cocolabs.dev/images/bofa_logo.png' }],
    ['meta', { property: 'og:url', content: 'https://mofa.cocolabs.dev' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:title', content: 'BOFA - Browser Overview Feed for Apple' }],
    ['meta', { name: 'twitter:description', content: 'Empowering Mac administrators with up-to-date browser version information for Apple devices' }],
    ['meta', { name: 'twitter:image', content: 'https://mofa.cocolabs.dev/images/bofa_logo.png' }],
    ['script', { async: '', src: 'https://www.googletagmanager.com/gtag/js?id=G-RQKDJ66BMC' }],
    ['script', {}, `
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-RQKDJ66BMC');
    `]
  ],
  themeConfig: {
    lastUpdated: true,
    cleanUrls: true,
    search: {
      provider: 'local'
    },
    editLink: {
      pattern: 'https://github.com/cocopuff2u/BOFA_website/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    },
    logo: '/images/bofa_logo.webp',
    nav: [
      { text: 'Get Started', link: '/home' },
      { text: 'Google Chrome', link: '/google_chrome/latest_versions' },
      { text: 'Mozilla Firefox', link: '/mozilla_firefox/latest_versions' },
      { text: 'Microsoft Edge', link: '/microsoft_edge/latest_versions' },
      { text: 'Safari', link: '/apple_safari/latest_versions' }
    ],
    sidebar: [
      {
      items: [
        { text: 'Get Started', link: '/home' }
      ]
      },
      {
        text: '<img src="/images/chrome.webp" style="height: 20px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Google Chrome',
        items: [
          { text: 'Overview', link: '/google_chrome/latest_versions'}]
      },
      {
        text: '<img src="/images/firefox.webp" style="height: 20px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Mozilla Firefox',
        items: [
          { text: 'Overview', link: '/mozilla_firefox/latest_versions'}]
      },
      {
        text: '<img src="/images/edge.webp" style="height: 20px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Microsoft Edge',
        items: [
          { text: 'Overview', link: '/microsoft_edge/latest_versions'}]
      },
      {
        text: '<img src="/images/safari.webp" style="height: 20px; display: inline-block; margin-right: 4px; vertical-align: text-bottom;"> Apple Safari',
        items: [
          { text: 'Overview', link: '/apple_safari/latest_versions'}]
      },
      {
        text: 'ℹ️ About & Support',
        collapsed: true,
        items: [
          { text: '📖 About', link: '/about_support/about' },
          { text: '📝 Feedback', link: '/about_support/feedback' },
          { text: '👥 Meet The Team', link: '/about_support/team' },
          { text: '🐞 Report Issues', link: '/about_support/report_issue' },
          { text: '🆕 Changelog', link: '/about_support/changelog' },
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/cocopuff2u/BOFA' },
      { icon: 'buymeacoffee', link: 'https://buymeacoffee.com/cocopuff2u' }
    ],
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2026 BOFA All rights reserved.'
    },
    markdown: {
      // Ensure HTML is enabled in markdown options
      html: true,
    }
  }
})
