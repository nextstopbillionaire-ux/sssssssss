# Video Resource Hub

A professional video link management application for YouTubers and content creators.

## Design Philosophy

Modern, professional design with:
- **Dark theme as default** (dark navy/blue backgrounds #1a1d2e)
- **Purple accent color** (#7c3aed - modern purple)
- **Generous spacing** and whitespace
- **Professional typography** with Inter font
- **Clean, minimal layout** for focus on content

## Features

### User Features
- **Hero Section**: Large, centered search for finding video links
- **Search by Video Link**: Paste video links to find associated resources/links
- **Quick Access Links**: Professional one-line layout with customizable action buttons (visible to all users)
- **Resource Cards**: 3-column grid with hover effects showing link count
- **10-Second Unlock**: Timed unlock mechanism for resource access
- **Copy/Open Links**: Each link has its own URL with copy and open actions
- **Theme Toggle**: Switch between dark and light modes

### Admin Features (Password: 111111)
- **Secret Admin Access**: Press Ctrl+Shift+A to open password prompt
- **Hidden UI Elements for Non-Admins**: 
  - "Add Resource" button hidden from navbar
  - "Add Link" button in Quick Access Links section hidden
  - Edit/Delete buttons hidden on all resources and links
- **Add Resources**: Create with display name, video link, and multiple link name+URL pairs
- **Edit Resources**: Update existing resources with name+URL pairs
- **Delete Resources**: Remove resources with confirmation
- **Manage Quick Links**: Add quick access links with name, URL, description, and customizable button text
- **Session Persistence**: Stays logged in until page refresh

## Layout Structure

### Navigation
- Logo on left with play icon
- Theme toggle on right (dark/light mode)
- "Add Resource" button is HIDDEN (secret access via Ctrl+Shift+A)
- Sticky positioning with subtle shadow

### Hero Section
- Large heading: "Find Your Video **Links**" (purple highlight on "Links")
- Subtitle: "Search, organize, and access your video links in one place"
- Prominent search bar with purple "Search" button
- Info card explaining the search functionality

### Main Content
- **Quick Access Links**: (Visible to all users, admin controls hidden)
  - Full-width items, one per line
  - Purple link icon, non-clickable title as text, description
  - Professional action button with customizable text (admin-defined, e.g., "Open in new tab", "Visit Now")
  - Button opens link in new tab with external link icon
  - Delete button on hover (admin only)
  - "Add Link" button visible for admins only
  
- **Available Resources**: 3-column grid
  - Play icon badge, display name, link count
  - Shows number of links (e.g., "3 link(s)")
  - Hover effects with purple border highlight
  - Edit/delete buttons on hover (admin only)

## Technical Details

### Color Palette (Dark Theme Default)
```
Primary Background: #1a1d2e (dark navy)
Secondary Background: #242938
Purple Accent: #7c3aed (buttons, highlights)
Text Primary: #f8f9fa (light text)
Text Secondary: #adb5bd
Border: #3a3a3a
Success: #28a745
Error: #dc3545
```

### Typography
- Font: Inter (400, 500, 600, 700, 800)
- Hero heading: 52px bold
- Section headings: 32-36px
- Body text: 14-16px

### Spacing System
- Navbar padding: 20px
- Hero padding: 80px vertical
- Section margins: 60-80px
- Card gaps: 24-32px

### Storage Structure
```javascript
// Resources (New Structure with Link Name+URL pairs)
{
  id: timestamp,
  outsideName: "Display name",
  videoLink: "Video URL to search by",
  links: [
    { name: "Link Name 1", url: "https://example.com/1" },
    { name: "Link Name 2", url: "https://example.com/2" }
  ]
}

// Quick Links (With Customizable Button Text)
{
  id: timestamp,
  name: "Link Name",
  url: "URL",
  description: "Optional description",
  buttonText: "Open in new tab" // Customizable button text (default: "Open in new tab")
}
```

### Data Migration
- Old resources with `titles` array are automatically migrated to new `links` structure
- Migration function converts each title to a link object with the resource's videoLink as the URL
- Backward compatibility maintained via `migrateResourceData()` function
- Old quick links without `buttonText` are automatically migrated with default value "Open in new tab"
- Migration function `migrateQuickLinksData()` ensures all quick links have a buttonText field

## Design Updates (October 2025)

Redesigned based on user-provided theme mockup:
- **Dark navy background** (#1a1d2e) as default theme
- **Purple accent colors** (#7c3aed) for modern, professional look
- **Quick Access Links Redesign**: 
  - Section now visible to all users (no longer admin-only)
  - Direct clickable links replaced with professional action buttons
  - Admin can customize button text (e.g., "Open in new tab", "Visit Now", "Learn More")
  - "Add Link" button visible only to admins
  - Non-clickable title with purple icon for clean, professional look
- **Admin-only controls**: 
  - "Add Resource" button removed from navbar for non-admins
  - Access admin features via Ctrl+Shift+A keyboard shortcut
  - Edit/Delete buttons hidden on resources and links for regular users
- **Enhanced link structure** - Resources now contain name+URL pairs instead of just titles
- **Improved terminology** - "Links" emphasized in search context for clarity
- Card-based organization with hover effects and purple highlights

## Responsive Design

- Desktop: 3-column grids (1200px max width)
- Tablet: 2-column grids (below 968px)
- Mobile: Single column (below 640px)
- Flexible navigation and search
