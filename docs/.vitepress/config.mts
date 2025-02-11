import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/',
  title: "MOFA",
  description: "Microsoft Overview For Apple",
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    ['script', { async: '', src: 'https://www.googletagmanager.com/gtag/js?id=G-P45L4Y5WFQ' }],
    ['script', {}, `
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-P45L4Y5WFQ');
    `]
  ],
  themeConfig: {
    lastUpdated: true,
    cleanUrls: true,
    search: {
      provider: 'local'
    },
    editLink: {
      pattern: 'https://github.com/cocopuff2u/mofa_website/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    },
    logo: '/images/logo_Mofa_NoBackground.png',
    nav: [
      { text: 'Get Started', link: '/home' },
      { text: 'Standalone Apps', link: '/standalone_apps/standalone_current_version_en' },
      { text: 'MacOS AppStore', link: '/macos_appstore/macos_appstore_current_version' },
      { text: 'iOS AppStore', link: '/ios_appstore/ios_appstore_current_version' }
    ],
    sidebar: [
      {
      items: [
        { text: 'Get Started', link: '/home' }
      ]
      },
      {
        text: '📦 Standalone Apps',
        collapsed: true,
        items: [
          { text: 'Current Versions', link: '/standalone_apps/standalone_current_version_en',
            collapsed: true,
            items: [
              { text: 'SHA1 Hashes', link: '/standalone_apps/standalone_sha1_hashes_en' },
              { text: 'SHA256 Hashes', link: '/standalone_apps/standalone_sha256_hashes_en' }
            ]
          },
          { text: 'Preview Versions', link: '/standalone_apps/standalone_preview_version_en',
            collapsed: true,
            items: [
              { text: 'SHA1 Hashes', link: '/standalone_apps/standalone_preview_sha1_hashes_en' },
              { text: 'SHA256 Hashes', link: '/standalone_apps/standalone_preview_sha256_hashes_en' }
            ]
          },
          { text: 'Beta Versions', link: '/standalone_apps/standalone_beta_version_en',
            collapsed: true,
            items: [
              { text: 'SHA1 Hashes', link: '/standalone_apps/standalone_beta_sha1_hashes_en' },
              { text: 'SHA256 Hashes', link: '/standalone_apps/standalone_beta_sha256_hashes_en' }
            ]
          },
          { text: 'Last Supported Versions', link: '/standalone_apps/standalone_last_supported_versions_en' },
          { text: 'Update History', link: '/standalone_apps/standalone_update_history_en' },
          { text: 'CVE (Vulnerabilities)', link: '/standalone_apps/standalone_cve_history_en' },
          { text: 'Raw Feeds', link: '/standalone_apps/standalone_raw_feeds_en' }
        ]
      },
      {
        text: '📚 MacOS Guides',
        collapsed: true,
        items: [
          {
            text: 'Mobile Device Management',
            collapsed: true,
            items: [
              { text: 'MDM Overview', link: '/placeholder' }
            ]
          },
          {
            text: 'How To Guides',
            collapsed: true,
            items: [
              { text: 'How To SHA1', link: '/guides/how_to_sha1' },
              { text: 'How To SHA256', link: '/guides/how_to_sha256' },
              { text: 'How To Plist', link: '/guides/how_to_plist' }
            ]
          }
        ]
      },
      {
                text: '🛠️ MacOS Tools',
        collapsed: true,
        items: [
          { text: 'Microsoft Office Repair Tools', link: '/macos_tools/microsoft_office_repair_tools' },
          { text: 'Community Scripts', link: '/macos_tools/community_scripts' },
          { text: 'Preconfigured Profiles', link: '/macos_tools/preconfigured_profiles',
            collapsed: true,
            items: [
              { text: 'Profile Breakdown', link: '/macos_tools/profile_breakdown' }
            ]
           }
        ]
      },
      {
        text: '💻 MacOS AppStore',
        collapsed: true,
        items: [
          { text: 'Current Version', link: '/macos_appstore/macos_appstore_current_version' },
          { text: 'Raw Feeds', link: '/macos_appstore/macos_raw_feeds' }
        ]
      },
      {
        text: '📱 iOS AppStore',
        collapsed: true,
        items: [
          { text: 'Current Version', link: '/ios_appstore/ios_appstore_current_version' },
          { text: 'Raw Feeds', link: '/ios_appstore/ios_raw_feeds' }
        ]
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
      { icon: 'github', link: 'https://github.com/cocopuff2u/MOFA' },
      { icon: 'buymeacoffee', link: 'https://buymeacoffee.com/cocopuff2u' }
    ],
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2025 MOFA All rights reserved.'
    },
    markdown: {
      // Ensure HTML is enabled in markdown options
      html: true,
    }
  }
})
