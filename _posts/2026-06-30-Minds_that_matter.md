---
title: "Minds that matter"
date: 2026-06-06
slug: "Minds that matter"
categories: [future]
tags: []
image:
  alt: 
---
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: #f4f5f8;
    color: #1a1d27;
    padding: 28px 20px 36px;
  }

  .header {
    text-align: center;
    margin-bottom: 28px;
  }
  .header h1 {
    font-size: 22px;
    font-weight: 800;
    color: #111318;
    margin-bottom: 5px;
  }
  .header p {
    font-size: 13px;
    color: #666980;
  }

  .domain-block { margin-bottom: 20px; }

  .domain-label {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 9px;
  }
  .domain-label .dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    flex-shrink: 0;
  }
  .domain-label .name {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.1px;
    text-transform: uppercase;
    color: #444657;
  }
  .domain-label .count {
    font-size: 10px;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 10px;
  }

  /* 2-row grid for AI block */
  .cards-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
  }

  /* Regular flex row for 2-person domains */
  .cards {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
  }

  .card {
    background: #ffffff;
    border-radius: 10px;
    padding: 14px 15px;
    border-top: 4px solid;
    box-shadow: 0 1px 4px rgba(0,0,0,0.07);
  }

  /* In flex rows, cards should grow equally */
  .cards .card { flex: 1; min-width: 155px; }

  .card-name {
    font-size: 14px;
    font-weight: 800;
    color: #111318;
    margin-bottom: 2px;
  }
  .card-role {
    font-size: 11px;
    color: #888ba0;
    font-weight: 500;
    margin-bottom: 8px;
  }
  .card-skill {
    font-size: 12px;
    line-height: 1.55;
    color: #333547;
  }
  .card-tag {
    display: inline-block;
    font-size: 10px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 6px;
    margin-top: 9px;
    letter-spacing: 0.2px;
  }

  /* Domain colours */
  .c-ai    { border-top-color: #4C6EF5; }
  .c-phil  { border-top-color: #9B59D0; }
  .c-econ  { border-top-color: #1CAB8A; }
  .c-art   { border-top-color: #E8722A; }
  .c-sci   { border-top-color: #2196C9; }
  .c-psych { border-top-color: #D4A017; }
  .c-pol   { border-top-color: #C94070; }

  .dot-ai    { background: #4C6EF5; }
  .dot-phil  { background: #9B59D0; }
  .dot-econ  { background: #1CAB8A; }
  .dot-art   { background: #E8722A; }
  .dot-sci   { background: #2196C9; }
  .dot-psych { background: #D4A017; }
  .dot-pol   { background: #C94070; }

  .cnt-ai    { background: #e8ecff; color: #3050C8; }
  .cnt-phil  { background: #f2eaff; color: #7B3DB0; }
  .cnt-econ  { background: #e0f8f2; color: #0E8A6E; }
  .cnt-art   { background: #fdf0e7; color: #C05818; }
  .cnt-sci   { background: #e3f4fb; color: #1576A5; }
  .cnt-psych { background: #fdf6e0; color: #A07800; }
  .cnt-pol   { background: #fde8ee; color: #A0204E; }

  .tag-ai    { background: #e8ecff; color: #3050C8; }
  .tag-phil  { background: #f2eaff; color: #7B3DB0; }
  .tag-econ  { background: #e0f8f2; color: #0E8A6E; }
  .tag-art   { background: #fdf0e7; color: #C05818; }
  .tag-sci   { background: #e3f4fb; color: #1576A5; }
  .tag-psych { background: #fdf6e0; color: #A07800; }
  .tag-pol   { background: #fde8ee; color: #A0204E; }

  .divider {
    height: 1px;
    background: #e0e2ea;
    margin: 20px 0;
  }

  .footer {
    text-align: center;
    font-size: 12px;
    color: #555770;
    margin-top: 26px;
    padding: 14px 16px;
    background: #fff;
    border-radius: 10px;
    line-height: 1.6;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
  }
  .footer strong { color: #111318; }
</style>



<div class="infographic-wrap">
<div class="header">
  <h1>Minds That Matter: Next 20 Years</h1>
  <p>18 figures across 7 domains — skills that compound as AI reshapes the world</p>
</div>

<!-- AI — 2 rows × 3 -->
<div class="domain-block">
  <div class="domain-label">
    <div class="dot dot-ai"></div>
    <span class="name">Artificial Intelligence</span>
    <span class="count cnt-ai">6 people</span>
  </div>
  <div class="cards-grid">
    <div class="card c-ai">
      <div class="card-name">Demis Hassabis</div>
      <div class="card-role">DeepMind / Nobel Laureate</div>
      <div class="card-skill">Bridges neuroscience + AI. AlphaFold solved a 50-year biology problem by combining two deep fields.</div>
      <span class="card-tag tag-ai">Cross-domain synthesis</span>
    </div>
    <div class="card c-ai">
      <div class="card-name">Andrej Karpathy</div>
      <div class="card-role">OpenAI · Tesla · Anthropic</div>
      <div class="card-skill">Understands AI from first principles and teaches it brilliantly. Rare builder + educator combination.</div>
      <span class="card-tag tag-ai">Technical education</span>
    </div>
    <div class="card c-ai">
      <div class="card-name">Ilya Sutskever</div>
      <div class="card-role">OpenAI co-founder / SSI</div>
      <div class="card-skill">AlexNet architect. Left OpenAI over safety convictions. Models intellectual courage in high-stakes settings.</div>
      <span class="card-tag tag-ai">AI safety thinking</span>
    </div>
    <div class="card c-ai">
      <div class="card-name">Yann LeCun</div>
      <div class="card-role">Meta AI / Turing Award</div>
      <div class="card-skill">Invented CNNs. Willing to hold contrarian views publicly. Teaches skepticism of consensus.</div>
      <span class="card-tag tag-ai">Architectural innovation</span>
    </div>
    <div class="card c-ai">
      <div class="card-name">Geoffrey Hinton</div>
      <div class="card-role">Godfather of Deep Learning</div>
      <div class="card-skill">Intellectual root of modern AI. Left Google to speak freely on existential risk. Models belief updating under new evidence.</div>
      <span class="card-tag tag-ai">Foundational reasoning</span>
    </div>
    <div class="card c-ai">
      <div class="card-name">Andrew Ng</div>
      <div class="card-role">Google Brain · Coursera · DeepLearning.AI</div>
      <div class="card-skill">Built AI education infrastructure for millions. Democratising technical skills at scale is one of the most leveraged acts of the next 20 years.</div>
      <span class="card-tag tag-ai">AI democratisation</span>
    </div>
  </div>
</div>

<div class="divider"></div>

<!-- Philosophy -->
<div class="domain-block">
  <div class="domain-label">
    <div class="dot dot-phil"></div>
    <span class="name">Philosophy</span>
    <span class="count cnt-phil">2 people</span>
  </div>
  <div class="cards">
    <div class="card c-phil">
      <div class="card-name">Marcus Aurelius</div>
      <div class="card-role">Roman Emperor · Stoic</div>
      <div class="card-skill">Most powerful man in the world, privately practicing humility daily. The original resilience framework under pressure.</div>
      <span class="card-tag tag-phil">Stoic resilience</span>
    </div>
    <div class="card c-phil">
      <div class="card-name">Hannah Arendt</div>
      <div class="card-role">Political Philosopher</div>
      <div class="card-skill">"Banality of evil" — how ordinary systems produce monstrous outcomes. Essential lens for AI governance and algorithmic harm.</div>
      <span class="card-tag tag-phil">Systems &amp; power</span>
    </div>
  </div>
</div>

<!-- Economics -->
<div class="domain-block">
  <div class="domain-label">
    <div class="dot dot-econ"></div>
    <span class="name">Economics</span>
    <span class="count cnt-econ">2 people</span>
  </div>
  <div class="cards">
    <div class="card c-econ">
      <div class="card-name">Daniel Kahneman</div>
      <div class="card-role">Nobel Laureate · Behavioral Econ</div>
      <div class="card-skill">System 1 vs. System 2 thinking: knowing when to trust fast intuition vs. slow deliberation. Critical for working with AI outputs.</div>
      <span class="card-tag tag-econ">Cognitive bias</span>
    </div>
    <div class="card c-econ">
      <div class="card-name">Clayton Christensen</div>
      <div class="card-role">Disruption Theory</div>
      <div class="card-skill">New tech underperforms then overtakes incumbents. The best map for how AI will move through industries over 20 years.</div>
      <span class="card-tag tag-econ">Disruption framework</span>
    </div>
  </div>
</div>

<!-- Art -->
<div class="domain-block">
  <div class="domain-label">
    <div class="dot dot-art"></div>
    <span class="name">Art &amp; Creativity</span>
    <span class="count cnt-art">2 people</span>
  </div>
  <div class="cards">
    <div class="card c-art">
      <div class="card-name">Leonardo da Vinci</div>
      <div class="card-role">Renaissance Polymath</div>
      <div class="card-skill">Unified art, anatomy, engineering and hydraulics in one mind. The original model for cross-domain thinking.</div>
      <span class="card-tag tag-art">Polymathic curiosity</span>
    </div>
    <div class="card c-art">
      <div class="card-name">Ursula K. Le Guin</div>
      <div class="card-role">Science Fiction Author</div>
      <div class="card-skill">Built entire societies with different economics and gender structures — rigorously. Models second-order AI consequence thinking.</div>
      <span class="card-tag tag-art">Speculative systems</span>
    </div>
  </div>
</div>

<!-- Science -->
<div class="domain-block">
  <div class="domain-label">
    <div class="dot dot-sci"></div>
    <span class="name">Science</span>
    <span class="count cnt-sci">2 people</span>
  </div>
  <div class="cards">
    <div class="card c-sci">
      <div class="card-name">Richard Feynman</div>
      <div class="card-role">Physicist · Educator</div>
      <div class="card-skill">If you can't explain it simply, you don't understand it. First-principles learning is the core human skill as AI handles surface knowledge.</div>
      <span class="card-tag tag-sci">First-principles thinking</span>
    </div>
    <div class="card c-sci">
      <div class="card-name">Carl Sagan</div>
      <div class="card-role">Astronomer · Communicator</div>
      <div class="card-skill">His Baloney Detection Kit is a practical manual for navigating AI-generated misinformation and epistemic pollution.</div>
      <span class="card-tag tag-sci">Critical scepticism</span>
    </div>
  </div>
</div>

<!-- Psychology -->
<div class="domain-block">
  <div class="domain-label">
    <div class="dot dot-psych"></div>
    <span class="name">Psychology</span>
    <span class="count cnt-psych">2 people</span>
  </div>
  <div class="cards">
    <div class="card c-psych">
      <div class="card-name">Viktor Frankl</div>
      <div class="card-role">Logotherapy · Holocaust Survivor</div>
      <div class="card-skill">Meaning — not pleasure — is the primary human motivator. When AI handles routine work, the question of meaning becomes central.</div>
      <span class="card-tag tag-psych">Meaning-making</span>
    </div>
    <div class="card c-psych">
      <div class="card-name">Carol Dweck</div>
      <div class="card-role">Stanford Psychologist</div>
      <div class="card-skill">Growth mindset: ability is expandable, not fixed. The psychological foundation for the continuous reskilling the next 20 years will demand.</div>
      <span class="card-tag tag-psych">Growth mindset</span>
    </div>
  </div>
</div>

<!-- Political Leadership -->
<div class="domain-block">
  <div class="domain-label">
    <div class="dot dot-pol"></div>
    <span class="name">Political Leadership</span>
    <span class="count cnt-pol">2 people</span>
  </div>
  <div class="cards">
    <div class="card c-pol">
      <div class="card-name">Nelson Mandela</div>
      <div class="card-role">President of South Africa</div>
      <div class="card-skill">27 years in prison, emerged choosing reconciliation over revenge. Long-term moral vision under extreme pressure.</div>
      <span class="card-tag tag-pol">Moral leadership</span>
    </div>
    <div class="card c-pol">
      <div class="card-name">Václav Havel</div>
      <div class="card-role">Playwright · Czech President</div>
      <div class="card-skill">"Living in truth" as resistance to systems built on lies. Directly applicable in a world of deepfakes and AI-generated propaganda.</div>
      <span class="card-tag tag-pol">Truth under power</span>
    </div>
  </div>
</div>

<div class="footer">
  <strong>Common thread across all 18:</strong> deep observational patience · comfort with uncertainty · skepticism of surface appearances · systems thinking
</div>
</div>
