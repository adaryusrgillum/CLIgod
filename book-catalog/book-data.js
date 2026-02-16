// Book Data for The Small Business AI Revolution Series

const booksData = [
    // Foundation Level (Books 1-3)
    {
        id: 1,
        title: "AI for the Rest of Us",
        subtitle: "First steps into AI for small business owners",
        category: "foundation",
        categoryName: "Foundation Level",
        description: "Your friendly introduction to AI without the jargon. Learn how AI can help your small business thrive.",
        pages: 150,
        color: "#667eea"
    },
    {
        id: 2,
        title: "Demystifying AI",
        subtitle: "What to know before getting started",
        category: "foundation",
        categoryName: "Foundation Level",
        description: "Clear explanations of AI concepts, separating hype from reality for practical business applications.",
        pages: 140,
        color: "#764ba2"
    },
    {
        id: 3,
        title: "The AI Mindset Shift",
        subtitle: "Preparing for the Intelligence Age",
        category: "foundation",
        categoryName: "Foundation Level",
        description: "Transform your thinking to embrace AI opportunities and prepare your business for the future.",
        pages: 160,
        color: "#f093fb"
    },
    
    // Strategy & Planning (Books 4-7)
    {
        id: 4,
        title: "The Small Business AI Roadmap",
        subtitle: "Strategy to implementation",
        category: "strategy",
        categoryName: "Strategy & Planning",
        description: "Step-by-step guide to planning and implementing AI in your business strategically.",
        pages: 180,
        color: "#4facfe"
    },
    {
        id: 5,
        title: "AI on a Budget",
        subtitle: "Smart strategies for cash-conscious companies",
        category: "strategy",
        categoryName: "Strategy & Planning",
        description: "Practical AI solutions that don't break the bank. Maximum impact with minimum investment.",
        pages: 145,
        color: "#00f2fe"
    },
    {
        id: 6,
        title: "Finding Your AI Advantage",
        subtitle: "Identifying high-impact opportunities",
        category: "strategy",
        categoryName: "Strategy & Planning",
        description: "Discover where AI can make the biggest difference in your specific business.",
        pages: 155,
        color: "#43e97b"
    },
    {
        id: 7,
        title: "The 90-Day AI Sprint",
        subtitle: "Implementation framework for small teams",
        category: "strategy",
        categoryName: "Strategy & Planning",
        description: "Fast-track your AI adoption with a proven 90-day implementation framework.",
        pages: 170,
        color: "#38f9d7"
    },
    
    // Operations & Automation (Books 8-11)
    {
        id: 8,
        title: "Automate to Liberate",
        subtitle: "Free yourself from repetitive tasks",
        category: "operations",
        categoryName: "Operations & Automation",
        description: "Use AI to automate routine tasks and focus on what matters most.",
        pages: 160,
        color: "#fa709a"
    },
    {
        id: 9,
        title: "The Invisible Workforce",
        subtitle: "AI agents working behind the scenes",
        category: "operations",
        categoryName: "Operations & Automation",
        description: "Build a team of AI agents that work 24/7 to support your operations.",
        pages: 165,
        color: "#fee140"
    },
    {
        id: 10,
        title: "Smart Operations",
        subtitle: "AI-optimized business processes",
        category: "operations",
        categoryName: "Operations & Automation",
        description: "Streamline every aspect of your operations with intelligent automation.",
        pages: 175,
        color: "#30cfd0"
    },
    {
        id: 11,
        title: "The Self-Running Business",
        subtitle: "Building autonomous systems",
        category: "operations",
        categoryName: "Operations & Automation",
        description: "Create systems that run themselves, giving you true business freedom.",
        pages: 185,
        color: "#330867"
    },
    
    // Marketing & Sales (Books 12-15)
    {
        id: 12,
        title: "AI-Powered Growth",
        subtitle: "Modern marketing for small business",
        category: "marketing",
        categoryName: "Marketing & Sales",
        description: "Leverage AI to supercharge your marketing and reach more customers.",
        pages: 170,
        color: "#f857a6"
    },
    {
        id: 13,
        title: "The Always-On Salesperson",
        subtitle: "AI sales assistance that never sleeps",
        category: "marketing",
        categoryName: "Marketing & Sales",
        description: "AI-powered sales tools that work around the clock to close deals.",
        pages: 155,
        color: "#ff5858"
    },
    {
        id: 14,
        title: "Predictive Profits",
        subtitle: "Using AI to forecast and influence outcomes",
        category: "marketing",
        categoryName: "Marketing & Sales",
        description: "Predict customer behavior and optimize your sales strategy with AI.",
        pages: 165,
        color: "#c471f5"
    },
    {
        id: 15,
        title: "Content at Scale",
        subtitle: "AI-assisted content creation",
        category: "marketing",
        categoryName: "Marketing & Sales",
        description: "Create high-quality content faster with AI assistance and automation.",
        pages: 150,
        color: "#fa709a"
    },
    
    // Customer Experience (Books 16-18)
    {
        id: 16,
        title: "The AI Concierge",
        subtitle: "Personalized customer experiences",
        category: "customer",
        categoryName: "Customer Experience",
        description: "Deliver personalized, VIP-level service to every customer with AI.",
        pages: 145,
        color: "#667eea"
    },
    {
        id: 17,
        title: "Knowing Your Customer",
        subtitle: "AI-driven insights and personalization",
        category: "customer",
        categoryName: "Customer Experience",
        description: "Understand your customers better than ever with AI-powered analytics.",
        pages: 160,
        color: "#764ba2"
    },
    {
        id: 18,
        title: "24/7 Service, Zero Headcount",
        subtitle: "Building intelligent customer support",
        category: "customer",
        categoryName: "Customer Experience",
        description: "Provide round-the-clock customer support without hiring a large team.",
        pages: 155,
        color: "#f093fb"
    },
    
    // Finance & Decision Making (Books 19-21)
    {
        id: 19,
        title: "The Crystal Ball CFO",
        subtitle: "Financial forecasting with AI",
        category: "finance",
        categoryName: "Finance & Decision Making",
        description: "Make better financial decisions with AI-powered forecasting and analysis.",
        pages: 165,
        color: "#4facfe"
    },
    {
        id: 20,
        title: "Data-Driven Decisions",
        subtitle: "AI analytics for small business",
        category: "finance",
        categoryName: "Finance & Decision Making",
        description: "Turn your business data into actionable insights with AI analytics.",
        pages: 170,
        color: "#00f2fe"
    },
    {
        id: 21,
        title: "Fraud Fighters",
        subtitle: "Protecting your business with AI",
        category: "finance",
        categoryName: "Finance & Decision Making",
        description: "Use AI to detect and prevent fraud, protecting your business assets.",
        pages: 140,
        color: "#43e97b"
    },
    
    // Industry-Specific (Books 22-27)
    {
        id: 22,
        title: "AI for Main Street",
        subtitle: "Retail-specific AI applications",
        category: "industry",
        categoryName: "Industry-Specific",
        description: "AI solutions tailored specifically for retail businesses.",
        pages: 175,
        color: "#38f9d7"
    },
    {
        id: 23,
        title: "Healing with Intelligence",
        subtitle: "AI for medical and wellness practices",
        category: "industry",
        categoryName: "Industry-Specific",
        description: "Transform healthcare and wellness practices with AI assistance.",
        pages: 180,
        color: "#fa709a"
    },
    {
        id: 24,
        title: "Built Smart",
        subtitle: "AI for construction and trades",
        category: "industry",
        categoryName: "Industry-Specific",
        description: "Apply AI to construction, contracting, and trade businesses.",
        pages: 170,
        color: "#fee140"
    },
    {
        id: 25,
        title: "The Intelligent Restaurant",
        subtitle: "AI in food service",
        category: "industry",
        categoryName: "Industry-Specific",
        description: "Optimize every aspect of restaurant operations with AI.",
        pages: 165,
        color: "#30cfd0"
    },
    {
        id: 26,
        title: "Legal AI",
        subtitle: "AI tools for attorneys",
        category: "industry",
        categoryName: "Industry-Specific",
        description: "Enhance legal practice efficiency with AI-powered tools.",
        pages: 185,
        color: "#330867"
    },
    {
        id: 27,
        title: "Creative Intelligence",
        subtitle: "AI for design and creative agencies",
        category: "industry",
        categoryName: "Industry-Specific",
        description: "Augment creativity and productivity in design and creative work.",
        pages: 160,
        color: "#f857a6"
    },
    
    // Advanced Implementation (Books 28-30)
    {
        id: 28,
        title: "Building Your AI Stack",
        subtitle: "Technical implementation guide",
        category: "advanced",
        categoryName: "Advanced Implementation",
        description: "Technical guide to building and integrating your AI technology stack.",
        pages: 195,
        color: "#ff5858"
    },
    {
        id: 29,
        title: "Training Your Business Brain",
        subtitle: "Custom AI models for your business",
        category: "advanced",
        categoryName: "Advanced Implementation",
        description: "Create custom AI models trained specifically for your business needs.",
        pages: 200,
        color: "#c471f5"
    },
    {
        id: 30,
        title: "The Human-AI Partnership",
        subtitle: "Optimizing collaboration",
        category: "advanced",
        categoryName: "Advanced Implementation",
        description: "Master the art of working alongside AI for maximum effectiveness.",
        pages: 175,
        color: "#fa709a"
    },
    
    // Ethics, Security & Future-Proofing (Books 31-33)
    {
        id: 31,
        title: "Responsible AI",
        subtitle: "Ethics and governance",
        category: "ethics",
        categoryName: "Ethics & Security",
        description: "Implement AI ethically and responsibly in your business.",
        pages: 165,
        color: "#667eea"
    },
    {
        id: 32,
        title: "Securing Your AI",
        subtitle: "Privacy and protection",
        category: "ethics",
        categoryName: "Ethics & Security",
        description: "Protect your AI systems and data with robust security practices.",
        pages: 170,
        color: "#764ba2"
    },
    {
        id: 33,
        title: "Future-Proof",
        subtitle: "Preparing for what's next",
        category: "ethics",
        categoryName: "Ethics & Security",
        description: "Stay ahead of AI trends and prepare your business for the future.",
        pages: 155,
        color: "#f093fb"
    },
    
    // Case Studies & Inspiration (Books 34-35)
    {
        id: 34,
        title: "Small Business, Big Intelligence",
        subtitle: "50 Success Stories",
        category: "case-studies",
        categoryName: "Case Studies",
        description: "Real-world success stories of small businesses transformed by AI.",
        pages: 220,
        color: "#4facfe"
    },
    {
        id: 35,
        title: "From Skeptic to Believer",
        subtitle: "Transformation journeys",
        category: "case-studies",
        categoryName: "Case Studies",
        description: "Inspiring stories of business owners who overcame AI skepticism.",
        pages: 180,
        color: "#00f2fe"
    },
    
    // Quick-Start Companion Series (Books 36-40)
    {
        id: 36,
        title: "AI in a Weekend",
        subtitle: "Quick start guide",
        category: "quick-start",
        categoryName: "Quick-Start",
        description: "Get started with AI in just one weekend with this practical guide.",
        pages: 120,
        color: "#43e97b"
    },
    {
        id: 37,
        title: "The $100 AI Makeover",
        subtitle: "Minimal investment, maximum impact",
        category: "quick-start",
        categoryName: "Quick-Start",
        description: "Transform your business with AI for under $100.",
        pages: 110,
        color: "#38f9d7"
    },
    {
        id: 38,
        title: "AI Tools Compared",
        subtitle: "Comprehensive comparison guide",
        category: "quick-start",
        categoryName: "Quick-Start",
        description: "Side-by-side comparison of popular AI tools for small business.",
        pages: 130,
        color: "#fa709a"
    },
    {
        id: 39,
        title: "The AI Implementation Checklist",
        subtitle: "Step-by-step action plan",
        category: "quick-start",
        categoryName: "Quick-Start",
        description: "Complete checklist to guide your AI implementation journey.",
        pages: 100,
        color: "#fee140"
    },
    {
        id: 40,
        title: "Talking to Your Team About AI",
        subtitle: "Communication and change management",
        category: "quick-start",
        categoryName: "Quick-Start",
        description: "Help your team embrace AI with effective communication strategies.",
        pages: 115,
        color: "#30cfd0"
    }
];

// Sample book content (for demonstration)
const sampleBookContent = {
    title: "",
    chapters: [
        {
            title: "Introduction",
            content: `Welcome to this transformative journey into the world of AI for small business.

This book is designed specifically for business owners who want to harness the power of artificial intelligence without needing a technical background. We'll explore practical applications, real-world examples, and actionable strategies you can implement immediately.

Throughout these pages, you'll discover how AI is no longer just for tech giants—it's accessible, affordable, and incredibly powerful for businesses of all sizes.

Let's begin this exciting adventure together.`
        },
        {
            title: "Chapter 1: Getting Started",
            content: `The first step in your AI journey is understanding what AI can realistically do for your business right now.

Forget the science fiction. We're talking about practical tools that can help you:
• Save time on repetitive tasks
• Better understand your customers
• Make smarter business decisions
• Compete with larger competitors

In this chapter, we'll explore the fundamentals and set realistic expectations for your AI transformation.

The best part? You don't need to be a technical expert. You just need to be open to new possibilities.`
        },
        {
            title: "Chapter 2: Understanding the Basics",
            content: `AI, or Artificial Intelligence, simply means computers performing tasks that normally require human intelligence.

For small business owners, this translates to:

1. **Automation**: Letting AI handle routine tasks
2. **Insights**: Using AI to analyze data and find patterns
3. **Personalization**: Tailoring experiences to each customer
4. **Optimization**: Making your operations more efficient

You don't need to understand how AI works under the hood—just like you don't need to know how your car engine works to drive it effectively.

What matters is knowing which AI tools can help your specific business needs.`
        }
    ]
};
