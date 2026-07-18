/**
 * Ask Enaasan Search Engine
 *
 * Client-side search for Enaasan publications
 * Philosophy: Students search for answers, not pages
 *
 * Searches against metadata in /metadata/publications/
 */

class AskEnaasan {
  constructor() {
    this.publications = [];
    this.loaded = false;
  }

  /**
   * Load all publication metadata
   */
  async loadMetadata() {
    try {
      const response = await fetch('/metadata/publications/index.json');
      const index = await response.json();

      // Load each publication metadata
      for (const pub of index.publications) {
        const pubResponse = await fetch(`/metadata/publications/${pub.file}`);
        const pubData = await pubResponse.json();
        this.publications.push(pubData);
      }

      this.loaded = true;
      console.log(`Ask Enaasan loaded ${this.publications.length} publications`);
    } catch (error) {
      console.error('Error loading Ask Enaasan metadata:', error);
    }
  }

  /**
   * Perform search
   * Matches against: title, keywords, questions, description, tags
   */
  search(query) {
    if (!this.loaded || !query.trim()) {
      return [];
    }

    const normalizedQuery = query.toLowerCase().trim();
    const queryTerms = normalizedQuery.split(/\s+/);

    const results = this.publications.map(pub => {
      let relevanceScore = 0;

      // Exact title match (high priority)
      if (pub.title.toLowerCase() === normalizedQuery) {
        relevanceScore += 100;
      }

      // Title contains query (high priority)
      if (pub.title.toLowerCase().includes(normalizedQuery)) {
        relevanceScore += 50;
      }

      // Check each query term
      queryTerms.forEach(term => {
        // Title match
        if (pub.title.toLowerCase().includes(term)) {
          relevanceScore += 10;
        }

        // Keyword match
        if (pub.keywords && pub.keywords.some(k => k.toLowerCase().includes(term))) {
          relevanceScore += 8;
        }

        // Question match
        if (pub.questions_it_answers && pub.questions_it_answers.some(q => q.toLowerCase().includes(term))) {
          relevanceScore += 7;
        }

        // Tag match
        if (pub.tags && pub.tags.some(t => t.toLowerCase().includes(term))) {
          relevanceScore += 6;
        }

        // Description match
        if (pub.description && pub.description.toLowerCase().includes(term)) {
          relevanceScore += 3;
        }
      });

      return {
        ...pub,
        relevanceScore
      };
    }).filter(result => result.relevanceScore > 0)
      .sort((a, b) => b.relevanceScore - a.relevanceScore);

    return results;
  }

  /**
   * Get featured publications for discovery
   */
  getFeatured() {
    return this.publications
      .filter(pub => pub.status === 'published')
      .slice(0, 6);
  }

  /**
   * Get coming soon publications
   */
  getComingSoon() {
    return this.publications.filter(pub => pub.status === 'coming-soon');
  }
}

// Initialize global instance
window.askEnaasan = new AskEnaasan();

// Load metadata when page loads
document.addEventListener('DOMContentLoaded', () => {
  window.askEnaasan.loadMetadata();
});
