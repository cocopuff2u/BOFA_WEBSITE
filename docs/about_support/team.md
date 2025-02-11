<script setup>
import { VPTeamMembers } from 'vitepress/theme'

const members = [
  {
    avatar: 'https://avatars.githubusercontent.com/u/95243190?s=96&v=4',
    name: 'Cody Keats',
    title: '✨ Lead Developer ✨',
    links: [
      { icon: 'github', link: 'https://github.com/cocopuff2u' },
      { icon: 'linkedin', link: 'https://linkedin.com/in/cody-keats' },
      { icon: 'slack', link: 'https://macadmins.slack.com/' }
    ]
  }
]

const members2 = [
  {
    avatar: 'https://avatars.githubusercontent.com/u/91097104?v=4',
    name: 'Darian Garcia',
    title: '💡 Contributor / Moral Support 💡',
    links: [
      { icon: 'github', link: 'https://github.com/darixn' },
    ]
  }
]
</script>

# 👥 Our Team

## 🌟 Core Developers 🌟

<VPTeamMembers size="medium" :members="members" />

## 🌈 Contributors 🌈

<VPTeamMembers size="medium" :members="members2" />

## 🚀 We Need Contributors! 🛠️

We're always looking for passionate people to contribute to the project. Whether you're a developer, designer, or just someone who loves working on open-source projects, we'd love to have you! 🧑‍💻🌍

### 🧑‍💻 Areas Where We Need Help:
- Adding new guides for MacOS App Store and iOS App Store apps 📱
- Improving & Adding raw data feeds 📊
- Creating more features for the website 🌐

The data powering this project is pulled from the repository [GitHub.com/cocopuff2u/mofa](https://github.com/cocopuff2u/mofa), and the website is hosted in its own repository at [GitHub.com/cocopuff2u/mofa_website](https://github.com/cocopuff2u/mofa_website).

Feel free to fork the repositories and contribute! You can open an issue or submit a pull request once you've made your updates. Let's make something great together! 🎉🚀



