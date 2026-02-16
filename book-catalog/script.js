// Main JavaScript for Book Catalog

let filteredBooks = [...booksData];
let currentBook = null;
let currentPage = 0;

// Initialize catalog on page load
document.addEventListener('DOMContentLoaded', () => {
    renderBookGrid();
    setupEventListeners();
});

// Setup event listeners
function setupEventListeners() {
    // Search functionality
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', (e) => {
        filterBooks();
    });
    
    // Category filter
    const categoryFilter = document.getElementById('categoryFilter');
    categoryFilter.addEventListener('change', () => {
        filterBooks();
    });
    
    // Reader controls
    document.getElementById('closeReader').addEventListener('click', closeReader);
    document.getElementById('prevPage').addEventListener('click', () => changePage(-1));
    document.getElementById('nextPage').addEventListener('click', () => changePage(1));
    document.getElementById('fullscreenBtn').addEventListener('click', toggleFullscreen);
    
    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
        if (document.getElementById('bookReader').classList.contains('hidden')) return;
        
        if (e.key === 'ArrowLeft') changePage(-1);
        if (e.key === 'ArrowRight') changePage(1);
        if (e.key === 'Escape') closeReader();
    });
}

// Filter books based on search and category
function filterBooks() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    const category = document.getElementById('categoryFilter').value;
    
    filteredBooks = booksData.filter(book => {
        const matchesSearch = book.title.toLowerCase().includes(searchTerm) ||
                            book.description.toLowerCase().includes(searchTerm);
        const matchesCategory = category === 'all' || book.category === category;
        
        return matchesSearch && matchesCategory;
    });
    
    renderBookGrid();
}

// Render book grid
function renderBookGrid() {
    const bookGrid = document.getElementById('bookGrid');
    
    if (filteredBooks.length === 0) {
        bookGrid.innerHTML = '<div class="loading">No books found matching your criteria</div>';
        return;
    }
    
    bookGrid.innerHTML = filteredBooks.map(book => `
        <div class="book-card" data-book-id="${book.id}">
            <div class="book-cover" style="background: linear-gradient(135deg, ${book.color} 0%, ${adjustColor(book.color, -20)} 100%);">
                <div class="book-number">Book ${book.id}</div>
                <div class="book-category">${book.categoryName}</div>
                <div class="book-title">${book.title}</div>
            </div>
            <div class="book-info">
                <h3>${book.title}</h3>
                <p class="book-description">${book.description}</p>
                <div class="book-meta">
                    <span class="meta-tag">📖 ${book.pages} pages</span>
                    <span class="meta-tag">${book.categoryName}</span>
                </div>
                <button class="read-btn" onclick="openBook(${book.id})">
                    📖 Read Preview
                </button>
            </div>
        </div>
    `).join('');
}

// Open book reader
function openBook(bookId) {
    currentBook = booksData.find(b => b.id === bookId);
    if (!currentBook) return;
    
    currentPage = 0;
    document.getElementById('bookReader').classList.remove('hidden');
    renderBook();
    updatePageIndicator();
}

// Close book reader
function closeReader() {
    document.getElementById('bookReader').classList.add('hidden');
    currentBook = null;
    currentPage = 0;
}

// Render book pages
function renderBook() {
    const flipbook = document.getElementById('flipbook');
    
    // Generate sample content for the book
    const pages = generateBookPages(currentBook);
    
    // Create page pairs (left and right)
    flipbook.innerHTML = '';
    
    for (let i = 0; i < pages.length; i += 2) {
        const pagePair = document.createElement('div');
        pagePair.className = 'page-pair';
        pagePair.style.display = i === currentPage ? 'block' : 'none';
        
        // Left page
        if (pages[i]) {
            const leftPage = createPage(pages[i], 'left');
            pagePair.appendChild(leftPage);
        }
        
        // Right page
        if (pages[i + 1]) {
            const rightPage = createPage(pages[i + 1], 'right');
            pagePair.appendChild(rightPage);
        }
        
        flipbook.appendChild(pagePair);
    }
}

// Create a single page element
function createPage(content, side) {
    const page = document.createElement('div');
    page.className = `page page-${side}`;
    page.innerHTML = `
        <div class="page-content">
            ${content}
        </div>
    `;
    return page;
}

// Generate book pages with sample content
function generateBookPages(book) {
    const pages = [];
    
    // Cover page
    pages.push(`
        <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100%; text-align: center;">
            <h1 style="font-size: 3rem; margin-bottom: 20px; color: ${book.color};">
                ${book.title}
            </h1>
            <p style="font-size: 1.5rem; color: #666; margin-bottom: 40px;">
                ${book.subtitle}
            </p>
            <div style="font-size: 1.2rem; color: #999;">
                Book ${book.id} of 40<br>
                ${book.categoryName}<br>
                ${book.pages} Pages
            </div>
        </div>
    `);
    
    // Table of contents
    pages.push(`
        <h1>Table of Contents</h1>
        <div style="margin-top: 30px;">
            <p style="margin: 15px 0;"><strong>Introduction</strong> ........... 1</p>
            <p style="margin: 15px 0;"><strong>Chapter 1:</strong> Getting Started ........... 5</p>
            <p style="margin: 15px 0;"><strong>Chapter 2:</strong> Understanding the Basics ........... 15</p>
            <p style="margin: 15px 0;"><strong>Chapter 3:</strong> Practical Applications ........... 30</p>
            <p style="margin: 15px 0;"><strong>Chapter 4:</strong> Implementation Strategy ........... 45</p>
            <p style="margin: 15px 0;"><strong>Chapter 5:</strong> Case Studies ........... 60</p>
            <p style="margin: 15px 0;"><strong>Chapter 6:</strong> Best Practices ........... 75</p>
            <p style="margin: 15px 0;"><strong>Chapter 7:</strong> Next Steps ........... 90</p>
            <p style="margin: 15px 0;"><strong>Conclusion</strong> ........... 100</p>
            <p style="margin: 15px 0;"><strong>Resources</strong> ........... 105</p>
        </div>
    `);
    
    // Introduction
    pages.push(`
        <h1>Introduction</h1>
        <p>Welcome to <em>${book.title}</em>, part of the comprehensive Small Business AI Revolution Series.</p>
        <p>${book.description}</p>
        <p>In this book, you'll discover practical strategies and actionable insights that you can implement immediately in your business. Whether you're just starting your AI journey or looking to expand your existing capabilities, this guide will provide the knowledge you need.</p>
        <h2>What You'll Learn</h2>
        <p>Throughout these pages, we'll explore:</p>
        <ul>
            <li>Fundamental concepts and terminology</li>
            <li>Real-world applications for small businesses</li>
            <li>Step-by-step implementation strategies</li>
            <li>Common pitfalls and how to avoid them</li>
            <li>Success stories and case studies</li>
            <li>Resources for continued learning</li>
        </ul>
    `);
    
    // Chapter 1
    pages.push(`
        <h1>Chapter 1: Getting Started</h1>
        <p>The journey of a thousand miles begins with a single step. Your AI transformation starts here.</p>
        <p>Before diving into complex implementations, it's crucial to understand where you are and where you want to go. This chapter will help you assess your current situation and define clear goals for your AI adoption.</p>
        <h2>Understanding Your Starting Point</h2>
        <p>Every business is unique, and your AI strategy should reflect that. Consider these questions:</p>
        <ul>
            <li>What are your biggest operational challenges?</li>
            <li>Where do you spend most of your time?</li>
            <li>What tasks feel repetitive or mundane?</li>
            <li>Where could better insights make a difference?</li>
        </ul>
        <p>The answers to these questions will guide your AI priorities and help you focus on high-impact opportunities.</p>
    `);
    
    // Additional sample pages
    pages.push(`
        <h2>Setting Realistic Expectations</h2>
        <p>AI is powerful, but it's not magic. Setting realistic expectations is crucial for success.</p>
        <p><strong>AI Can:</strong></p>
        <ul>
            <li>Automate repetitive tasks</li>
            <li>Analyze large amounts of data quickly</li>
            <li>Provide predictions based on patterns</li>
            <li>Personalize customer experiences</li>
            <li>Optimize operations and processes</li>
        </ul>
        <p><strong>AI Cannot:</strong></p>
        <ul>
            <li>Replace human judgment entirely</li>
            <li>Understand context without training</li>
            <li>Work without proper data</li>
            <li>Solve problems it wasn't designed for</li>
        </ul>
    `);
    
    pages.push(`
        <h2>The AI Mindset</h2>
        <p>Adopting AI successfully requires a shift in thinking. Instead of asking "Can AI do this?" ask "How can AI help me do this better?"</p>
        <p>This mindset shift is about augmentation, not replacement. AI should amplify your capabilities, free your time, and help you focus on what matters most: growing your business and serving your customers.</p>
        <h2>Your First Steps</h2>
        <p>Ready to begin? Here's your action plan:</p>
        <ol>
            <li><strong>Identify</strong> one problem you want to solve</li>
            <li><strong>Research</strong> AI tools that address this problem</li>
            <li><strong>Test</strong> a solution with a small pilot project</li>
            <li><strong>Measure</strong> the results</li>
            <li><strong>Scale</strong> what works</li>
        </ol>
    `);
    
    // Add more sample pages
    for (let i = 0; i < 10; i++) {
        pages.push(`
            <h1>Chapter ${i + 2}: Sample Content</h1>
            <p>This is a preview of the book content. The full book contains comprehensive information, detailed examples, practical exercises, and real-world case studies.</p>
            <p>Each chapter is carefully crafted to provide maximum value while being easy to understand and implement.</p>
            <h2>Key Takeaways</h2>
            <ul>
                <li>Practical insights you can use immediately</li>
                <li>Step-by-step guidance for implementation</li>
                <li>Real-world examples from small businesses</li>
                <li>Actionable strategies and tactics</li>
            </ul>
            <p>Continue reading to discover more valuable content designed specifically for small business owners like you.</p>
        `);
    }
    
    // Conclusion
    pages.push(`
        <h1>Conclusion</h1>
        <p>Congratulations on completing <em>${book.title}</em>!</p>
        <p>You now have the knowledge and tools to move forward confidently in your AI journey. Remember, this is just the beginning—AI is constantly evolving, and there's always more to learn.</p>
        <h2>Next Steps</h2>
        <p>Continue your learning with the other books in the Small Business AI Revolution Series. Each book builds on the previous ones, creating a comprehensive guide to AI adoption and implementation.</p>
        <p>Take action today. Start small, learn continuously, and watch your business transform.</p>
    `);
    
    return pages;
}

// Change page with animation
function changePage(direction) {
    const pages = document.querySelectorAll('.page-pair');
    const newPage = currentPage + (direction * 2);
    
    if (newPage < 0 || newPage >= pages.length * 2) return;
    
    // Hide current pages
    pages[Math.floor(currentPage / 2)].style.display = 'none';
    
    // Update current page
    currentPage = newPage;
    
    // Show new pages
    pages[Math.floor(currentPage / 2)].style.display = 'block';
    
    // Add flip animation
    animatePageFlip(direction);
    
    updatePageIndicator();
}

// Animate page flip
function animatePageFlip(direction) {
    const pages = document.querySelectorAll('.page');
    pages.forEach(page => {
        page.classList.add('flipping');
        setTimeout(() => {
            page.classList.remove('flipping');
        }, 800);
    });
}

// Update page indicator
function updatePageIndicator() {
    const totalPages = Math.ceil(generateBookPages(currentBook).length / 2) * 2;
    document.getElementById('pageIndicator').textContent = 
        `Page ${currentPage + 1}-${Math.min(currentPage + 2, totalPages)} of ${totalPages}`;
}

// Toggle fullscreen
function toggleFullscreen() {
    const reader = document.getElementById('bookReader');
    
    if (!document.fullscreenElement) {
        reader.requestFullscreen().catch(err => {
            console.log('Fullscreen request failed:', err);
        });
    } else {
        document.exitFullscreen();
    }
}

// Utility function to adjust color brightness
function adjustColor(color, amount) {
    const num = parseInt(color.replace('#', ''), 16);
    const r = Math.max(0, Math.min(255, (num >> 16) + amount));
    const g = Math.max(0, Math.min(255, ((num >> 8) & 0x00FF) + amount));
    const b = Math.max(0, Math.min(255, (num & 0x0000FF) + amount));
    return '#' + ((r << 16) | (g << 8) | b).toString(16).padStart(6, '0');
}

// Make openBook globally accessible
window.openBook = openBook;
