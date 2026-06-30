---
title: "Minds that matter"
date: 2026-06-06
slug: "Minds that matter"
categories: [future]
toc: false
---

<style>
  .infographic-wrap * { box-sizing: border-box; }
  .infographic-wrap {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    background: #f0f2f7;
    color: #1a1d27;
    padding: 28px 20px 40px;
    border-radius: 16px;
    margin: 0 -8px;
  }
  .infographic-wrap .header { text-align: center; margin-bottom: 28px; }
  .infographic-wrap .header h2 { font-size: 22px; font-weight: 800; color: #111318; margin-bottom: 5px; border: none; padding: 0; }
  .infographic-wrap .header p { font-size: 13px; color: #666980; }

  .infographic-wrap .domain-block { margin-bottom: 22px; }
  .infographic-wrap .domain-label { display: flex; align-items: center; gap: 8px; margin-bottom: 10px; }
  .infographic-wrap .domain-label .dot { width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }
  .infographic-wrap .domain-label .dname { font-size: 11px; font-weight: 700; letter-spacing: 1.1px; text-transform: uppercase; color: #444657; }
  .infographic-wrap .domain-label .count { font-size: 10px; font-weight: 700; padding: 2px 7px; border-radius: 10px; }

  .infographic-wrap .cards-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
  .infographic-wrap .cards { display: flex; gap: 10px; flex-wrap: wrap; }
  .infographic-wrap .cards .card { flex: 1; min-width: 155px; }

  .infographic-wrap .card {
    background: #ffffff;
    border-radius: 12px;
    padding: 16px 14px 14px;
    border-top: 4px solid;
    box-shadow: 0 1px 4px rgba(0,0,0,0.07);
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
  }

  .infographic-wrap .avatar-link {
    display: block; margin-bottom: 10px; border-radius: 50%;
    overflow: hidden; width: 64px; height: 64px; flex-shrink: 0; border: 3px solid;
  }
  .infographic-wrap .avatar-link img { width: 100%; height: 100%; object-fit: cover; display: block; }
  .infographic-wrap .avatar-fallback {
    width: 64px; height: 64px; border-radius: 50%; margin-bottom: 10px;
    border: 3px solid; display: flex; align-items: center; justify-content: center;
    font-size: 20px; font-weight: 800; color: #fff; flex-shrink: 0;
  }

  .infographic-wrap .card-name { font-size: 13px; font-weight: 800; color: #111318; margin-bottom: 2px; }
  .infographic-wrap .card-role { font-size: 10.5px; color: #888ba0; font-weight: 500; margin-bottom: 8px; }
  .infographic-wrap .card-skill { font-size: 11px; line-height: 1.55; color: #333547; text-align: left; }
  .infographic-wrap .card-tag { display: inline-block; font-size: 10px; font-weight: 700; padding: 3px 8px; border-radius: 6px; margin-top: 9px; }

  .infographic-wrap .divider { height: 1px; background: #e0e2ea; margin: 20px 0; }

  .infographic-wrap .inf-footer {
    text-align: center; font-size: 12px; color: #555770;
    margin-top: 26px; padding: 14px 16px; background: #fff;
    border-radius: 10px; line-height: 1.7;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
  }
  .infographic-wrap .inf-footer strong { color: #111318; }
  .infographic-wrap .inf-footer a { color: #4C6EF5; text-decoration: none; }

  /* Domain border colours */
  .infographic-wrap .c-ai    { border-top-color: #4C6EF5; }
  .infographic-wrap .c-phil  { border-top-color: #9B59D0; }
  .infographic-wrap .c-econ  { border-top-color: #1CAB8A; }
  .infographic-wrap .c-art   { border-top-color: #E8722A; }
  .infographic-wrap .c-sci   { border-top-color: #2196C9; }
  .infographic-wrap .c-psych { border-top-color: #D4A017; }
  .infographic-wrap .c-pol   { border-top-color: #C94070; }

  /* Avatar ring + fallback background */
  .infographic-wrap .av-ai    { border-color: #4C6EF5; background: #4C6EF5; }
  .infographic-wrap .av-phil  { border-color: #9B59D0; background: #9B59D0; }
  .infographic-wrap .av-econ  { border-color: #1CAB8A; background: #1CAB8A; }
  .infographic-wrap .av-art   { border-color: #E8722A; background: #E8722A; }
  .infographic-wrap .av-sci   { border-color: #2196C9; background: #2196C9; }
  .infographic-wrap .av-psych { border-color: #D4A017; background: #D4A017; }
  .infographic-wrap .av-pol   { border-color: #C94070; background: #C94070; }

  /* Domain dot colours */
  .infographic-wrap .dot-ai    { background: #4C6EF5; }
  .infographic-wrap .dot-phil  { background: #9B59D0; }
  .infographic-wrap .dot-econ  { background: #1CAB8A; }
  .infographic-wrap .dot-art   { background: #E8722A; }
  .infographic-wrap .dot-sci   { background: #2196C9; }
  .infographic-wrap .dot-psych { background: #D4A017; }
  .infographic-wrap .dot-pol   { background: #C94070; }

  /* Count badge colours */
  .infographic-wrap .cnt-ai    { background: #e8ecff; color: #3050C8; }
  .infographic-wrap .cnt-phil  { background: #f2eaff; color: #7B3DB0; }
  .infographic-wrap .cnt-econ  { background: #e0f8f2; color: #0E8A6E; }
  .infographic-wrap .cnt-art   { background: #fdf0e7; color: #C05818; }
  .infographic-wrap .cnt-sci   { background: #e3f4fb; color: #1576A5; }
  .infographic-wrap .cnt-psych { background: #fdf6e0; color: #A07800; }
  .infographic-wrap .cnt-pol   { background: #fde8ee; color: #A0204E; }

  /* Tag colours */
  .infographic-wrap .tag-ai    { background: #e8ecff; color: #3050C8; }
  .infographic-wrap .tag-phil  { background: #f2eaff; color: #7B3DB0; }
  .infographic-wrap .tag-econ  { background: #e0f8f2; color: #0E8A6E; }
  .infographic-wrap .tag-art   { background: #fdf0e7; color: #C05818; }
  .infographic-wrap .tag-sci   { background: #e3f4fb; color: #1576A5; }
  .infographic-wrap .tag-psych { background: #fdf6e0; color: #A07800; }
  .infographic-wrap .tag-pol   { background: #fde8ee; color: #A0204E; }

  /* Responsive: stack AI grid to 2 cols on small screens */
  @media (max-width: 640px) {
    .infographic-wrap .cards-grid { grid-template-columns: repeat(2, 1fr); }
    .infographic-wrap .cards .card { min-width: 140px; }
  }
  @media (max-width: 420px) {
    .infographic-wrap .cards-grid { grid-template-columns: 1fr; }
  }
</style>

<div class="infographic-wrap">

  <div class="header">
    <h2>Minds That Matter: Next 20 Years</h2>
    <p>18 figures across 7 domains — skills that compound as AI reshapes the world</p>
  </div>

  <!-- ── AI 2×3 ── -->
  <div class="domain-block">
    <div class="domain-label">
      <div class="dot dot-ai"></div>
      <span class="dname">Artificial Intelligence</span>
      <span class="count cnt-ai">6 people</span>
    </div>
    <div class="cards-grid">

      <div class="card c-ai">
        <a class="avatar-link av-ai" href="https://commons.wikimedia.org/wiki/File:Demis_Hassabis_Royal_Society_(3x4_cropped).jpg" title="The Royal Society, CC BY-SA 3.0, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Demis_Hassabis_Royal_Society_%283x4_cropped%29.jpg/250px-Demis_Hassabis_Royal_Society_%283x4_cropped%29.jpg" alt="Demis Hassabis" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-ai" style="display:none">DH</div>
        <div class="card-name">Demis Hassabis</div>
        <div class="card-role">DeepMind / Nobel Laureate</div>
        <div class="card-skill">Bridges neuroscience + AI. AlphaFold solved a 50-year biology problem by combining two deep fields.</div>
        <span class="card-tag tag-ai">Cross-domain synthesis</span>
      </div>

      <div class="card c-ai">
        <a class="avatar-link av-ai" href="https://commons.wikimedia.org/wiki/File:Andrej_Karpathy,_OpenAI_(cropped).png" title="Gladwin Analytics, CC BY 3.0, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Andrej_Karpathy%2C_OpenAI_%28cropped%29.png/250px-Andrej_Karpathy%2C_OpenAI_%28cropped%29.png" alt="Andrej Karpathy" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-ai" style="display:none">AK</div>
        <div class="card-name">Andrej Karpathy</div>
        <div class="card-role">OpenAI · Tesla · Anthropic</div>
        <div class="card-skill">Understands AI from first principles and teaches it brilliantly. Rare builder + educator combination.</div>
        <span class="card-tag tag-ai">Technical education</span>
      </div>

      <div class="card c-ai">
        <a class="avatar-link av-ai" href="https://commons.wikimedia.org/wiki/File:Ilya_Sutskever_and_Sam_Altman_in_TAU_(cropped).jpg" title="Amir Zuk, CC BY-SA 4.0, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Ilya_Sutskever_and_Sam_Altman_in_TAU_%28cropped%29.jpg/250px-Ilya_Sutskever_and_Sam_Altman_in_TAU_%28cropped%29.jpg" alt="Ilya Sutskever" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-ai" style="display:none">IS</div>
        <div class="card-name">Ilya Sutskever</div>
        <div class="card-role">OpenAI co-founder / SSI</div>
        <div class="card-skill">AlexNet architect. Left OpenAI over safety convictions. Models intellectual courage in high-stakes settings.</div>
        <span class="card-tag tag-ai">AI safety thinking</span>
      </div>

      <div class="card c-ai">
        <a class="avatar-link av-ai" href="https://commons.wikimedia.org/wiki/File:Yann_LeCun_-_2018_(cropped).jpg" title="Frankie Fouganthin, CC BY-SA 4.0, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Yann_LeCun_-_2018_%28cropped%29.jpg/250px-Yann_LeCun_-_2018_%28cropped%29.jpg" alt="Yann LeCun" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-ai" style="display:none">YL</div>
        <div class="card-name">Yann LeCun</div>
        <div class="card-role">Meta AI / Turing Award</div>
        <div class="card-skill">Invented CNNs. Willing to hold contrarian views publicly. Teaches skepticism of consensus.</div>
        <span class="card-tag tag-ai">Architectural innovation</span>
      </div>

      <div class="card c-ai">
        <a class="avatar-link av-ai" href="https://commons.wikimedia.org/wiki/File:Geoffrey_E._Hinton,_2024_Nobel_Prize_Laureate_in_Physics.jpg" title="Annika Bergman Rosamond / Nobel Prize Outreach, CC BY-SA 4.0, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Geoffrey_E._Hinton%2C_2024_Nobel_Prize_Laureate_in_Physics.jpg/250px-Geoffrey_E._Hinton%2C_2024_Nobel_Prize_Laureate_in_Physics.jpg" alt="Geoffrey Hinton" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-ai" style="display:none">GH</div>
        <div class="card-name">Geoffrey Hinton</div>
        <div class="card-role">Godfather of Deep Learning</div>
        <div class="card-skill">Intellectual root of modern AI. Left Google to speak freely on existential risk. Models belief updating under new evidence.</div>
        <span class="card-tag tag-ai">Foundational reasoning</span>
      </div>

      <div class="card c-ai">
        <a class="avatar-link av-ai" href="https://commons.wikimedia.org/wiki/File:Andrew_Ng.png" title="The Source, CC BY 3.0 US, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Andrew_Ng.png/250px-Andrew_Ng.png" alt="Andrew Ng" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-ai" style="display:none">AN</div>
        <div class="card-name">Andrew Ng</div>
        <div class="card-role">Google Brain · Coursera · DeepLearning.AI</div>
        <div class="card-skill">Built AI education infrastructure for millions. Democratising technical skills at scale is one of the highest-leverage acts of the next 20 years.</div>
        <span class="card-tag tag-ai">AI democratisation</span>
      </div>

    </div>
  </div><!-- /AI -->

  <div class="divider"></div>

  <!-- Philosophy -->
  <div class="domain-block">
    <div class="domain-label">
      <div class="dot dot-phil"></div>
      <span class="dname">Philosophy</span>
      <span class="count cnt-phil">2 people</span>
    </div>
    <div class="cards">
      <div class="card c-phil">
        <a class="avatar-link av-phil" href="https://commons.wikimedia.org/wiki/File:Portrait_of_Marcus_Aurelius.jpg" title="Marie-Lan Nguyen, Public domain, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Portrait_of_Marcus_Aurelius.jpg/250px-Portrait_of_Marcus_Aurelius.jpg" alt="Marcus Aurelius" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-phil" style="display:none">MA</div>
        <div class="card-name">Marcus Aurelius</div>
        <div class="card-role">Roman Emperor · Stoic</div>
        <div class="card-skill">Most powerful man in the world, privately practicing humility daily. The original resilience framework under pressure.</div>
        <span class="card-tag tag-phil">Stoic resilience</span>
      </div>
      <div class="card c-phil">
        <a class="avatar-link av-phil" href="https://commons.wikimedia.org/wiki/File:Hannah_Arendt_1975_(cropped).jpg" title="Dürr / Spiegel, CC BY-SA 3.0 DE, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Hannah_Arendt_1975_%28cropped%29.jpg/250px-Hannah_Arendt_1975_%28cropped%29.jpg" alt="Hannah Arendt" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-phil" style="display:none">HA</div>
        <div class="card-name">Hannah Arendt</div>
        <div class="card-role">Political Philosopher</div>
        <div class="card-skill">"Banality of evil" — how ordinary systems produce monstrous outcomes. Essential lens for AI governance and algorithmic harm.</div>
        <span class="card-tag tag-phil">Systems &amp; power</span>
      </div>
    </div>
  </div><!-- /Philosophy -->

  <!-- Economics -->
  <div class="domain-block">
    <div class="domain-label">
      <div class="dot dot-econ"></div>
      <span class="dname">Economics</span>
      <span class="count cnt-econ">2 people</span>
    </div>
    <div class="cards">
      <div class="card c-econ">
        <a class="avatar-link av-econ" href="https://commons.wikimedia.org/wiki/File:Daniel_Kahneman_(3283955327).jpg" title="Fronteiras do Pensamento, CC BY-SA 2.0, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Daniel_Kahneman_%283283955327%29.jpg/250px-Daniel_Kahneman_%283283955327%29.jpg" alt="Daniel Kahneman" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-econ" style="display:none">DK</div>
        <div class="card-name">Daniel Kahneman</div>
        <div class="card-role">Nobel Laureate · Behavioral Econ</div>
        <div class="card-skill">System 1 vs. System 2 thinking: knowing when to trust fast intuition vs. slow deliberation. Critical for working with AI outputs.</div>
        <span class="card-tag tag-econ">Cognitive bias</span>
      </div>
      <div class="card c-econ">
        <a class="avatar-link av-econ" href="https://commons.wikimedia.org/wiki/File:Clayton_Christensen_World_Economic_Forum_2013.jpg" title="World Economic Forum, CC BY-SA 2.0, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Clayton_Christensen_World_Economic_Forum_2013.jpg/250px-Clayton_Christensen_World_Economic_Forum_2013.jpg" alt="Clayton Christensen" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-econ" style="display:none">CC</div>
        <div class="card-name">Clayton Christensen</div>
        <div class="card-role">Disruption Theory</div>
        <div class="card-skill">New tech underperforms then overtakes incumbents. The best map for how AI will move through industries over 20 years.</div>
        <span class="card-tag tag-econ">Disruption framework</span>
      </div>
    </div>
  </div><!-- /Economics -->

  <!-- Art -->
  <div class="domain-block">
    <div class="domain-label">
      <div class="dot dot-art"></div>
      <span class="dname">Art &amp; Creativity</span>
      <span class="count cnt-art">2 people</span>
    </div>
    <div class="cards">
      <div class="card c-art">
        <a class="avatar-link av-art" href="https://commons.wikimedia.org/wiki/File:Leonardo_self.jpg" title="Leonardo da Vinci, Public domain, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Leonardo_self.jpg/250px-Leonardo_self.jpg" alt="Leonardo da Vinci" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-art" style="display:none">LV</div>
        <div class="card-name">Leonardo da Vinci</div>
        <div class="card-role">Renaissance Polymath</div>
        <div class="card-skill">Unified art, anatomy, engineering and hydraulics in one mind. The original model for cross-domain thinking.</div>
        <span class="card-tag tag-art">Polymathic curiosity</span>
      </div>
      <div class="card c-art">
        <a class="avatar-link av-art" href="https://commons.wikimedia.org/wiki/File:Ursula_Le_Guin_(3551195631)_(cropped).jpg" title="Hajor, CC BY-SA 3.0, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Ursula_Le_Guin_%283551195631%29_%28cropped%29.jpg/250px-Ursula_Le_Guin_%283551195631%29_%28cropped%29.jpg" alt="Ursula K. Le Guin" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-art" style="display:none">UL</div>
        <div class="card-name">Ursula K. Le Guin</div>
        <div class="card-role">Science Fiction Author</div>
        <div class="card-skill">Built entire societies with different economics and structures — rigorously. Models second-order AI consequence thinking.</div>
        <span class="card-tag tag-art">Speculative systems</span>
      </div>
    </div>
  </div><!-- /Art -->

  <!-- Science -->
  <div class="domain-block">
    <div class="domain-label">
      <div class="dot dot-sci"></div>
      <span class="dname">Science</span>
      <span class="count cnt-sci">2 people</span>
    </div>
    <div class="cards">
      <div class="card c-sci">
        <a class="avatar-link av-sci" href="https://commons.wikimedia.org/wiki/File:Richard_Feynman_1959.png" title="Caltech, Public domain, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Richard_Feynman_1959.png/250px-Richard_Feynman_1959.png" alt="Richard Feynman" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-sci" style="display:none">RF</div>
        <div class="card-name">Richard Feynman</div>
        <div class="card-role">Physicist · Educator</div>
        <div class="card-skill">If you can't explain it simply, you don't understand it. First-principles learning is the core human skill as AI handles surface knowledge.</div>
        <span class="card-tag tag-sci">First-principles thinking</span>
      </div>
      <div class="card c-sci">
        <a class="avatar-link av-sci" href="https://commons.wikimedia.org/wiki/File:Carl_Sagan_Planetary_Society.JPG" title="The Planetary Society, CC BY-SA 3.0, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Carl_Sagan_Planetary_Society.JPG/250px-Carl_Sagan_Planetary_Society.JPG" alt="Carl Sagan" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-sci" style="display:none">CS</div>
        <div class="card-name">Carl Sagan</div>
        <div class="card-role">Astronomer · Communicator</div>
        <div class="card-skill">His Baloney Detection Kit is a practical manual for navigating AI-generated misinformation and epistemic pollution.</div>
        <span class="card-tag tag-sci">Critical scepticism</span>
      </div>
    </div>
  </div><!-- /Science -->

  <!-- Psychology -->
  <div class="domain-block">
    <div class="domain-label">
      <div class="dot dot-psych"></div>
      <span class="dname">Psychology</span>
      <span class="count cnt-psych">2 people</span>
    </div>
    <div class="cards">
      <div class="card c-psych">
        <a class="avatar-link av-psych" href="https://commons.wikimedia.org/wiki/File:Viktor_Frankl2.jpg" title="Prof. Dr. Franz Vesely, CC BY-SA 3.0 AT, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Viktor_Frankl2.jpg/250px-Viktor_Frankl2.jpg" alt="Viktor Frankl" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-psych" style="display:none">VF</div>
        <div class="card-name">Viktor Frankl</div>
        <div class="card-role">Logotherapy · Holocaust Survivor</div>
        <div class="card-skill">Meaning — not pleasure — is the primary human motivator. When AI handles routine work, the question of meaning becomes central.</div>
        <span class="card-tag tag-psych">Meaning-making</span>
      </div>
      <div class="card c-psych">
        <a class="avatar-link av-psych" href="https://commons.wikimedia.org/wiki/File:Carol_Dweck_for_Innovation_documentary.jpg" title="Innovation documentary, CC BY 3.0, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Carol_Dweck_for_Innovation_documentary.jpg/250px-Carol_Dweck_for_Innovation_documentary.jpg" alt="Carol Dweck" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-psych" style="display:none">CD</div>
        <div class="card-name">Carol Dweck</div>
        <div class="card-role">Stanford Psychologist</div>
        <div class="card-skill">Growth mindset: ability is expandable, not fixed. The psychological foundation for continuous reskilling the next 20 years will demand.</div>
        <span class="card-tag tag-psych">Growth mindset</span>
      </div>
    </div>
  </div><!-- /Psychology -->

  <!-- Political Leadership -->
  <div class="domain-block">
    <div class="domain-label">
      <div class="dot dot-pol"></div>
      <span class="dname">Political Leadership</span>
      <span class="count cnt-pol">2 people</span>
    </div>
    <div class="cards">
      <div class="card c-pol">
        <a class="avatar-link av-pol" href="https://commons.wikimedia.org/wiki/File:Nelson_Mandela-2008_(edit).jpg" title="South Africa The Good News, CC BY 2.0, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Nelson_Mandela-2008_%28edit%29.jpg/250px-Nelson_Mandela-2008_%28edit%29.jpg" alt="Nelson Mandela" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-pol" style="display:none">NM</div>
        <div class="card-name">Nelson Mandela</div>
        <div class="card-role">President of South Africa</div>
        <div class="card-skill">27 years in prison, emerged choosing reconciliation over revenge. Long-term moral vision under extreme pressure.</div>
        <span class="card-tag tag-pol">Moral leadership</span>
      </div>
      <div class="card c-pol">
        <a class="avatar-link av-pol" href="https://commons.wikimedia.org/wiki/File:Vaclav_Havel.jpg" title="Krokodyl, CC BY-SA 3.0, via Wikimedia Commons" target="_blank">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Vaclav_Havel.jpg/250px-Vaclav_Havel.jpg" alt="Václav Havel" onerror="this.parentElement.style.display='none';this.parentElement.nextElementSibling.style.display='flex'">
        </a>
        <div class="avatar-fallback av-pol" style="display:none">VH</div>
        <div class="card-name">Václav Havel</div>
        <div class="card-role">Playwright · Czech President</div>
        <div class="card-skill">"Living in truth" as resistance to systems built on lies. Directly applicable in a world of deepfakes and AI-generated propaganda.</div>
        <span class="card-tag tag-pol">Truth under power</span>
      </div>
    </div>
  </div><!-- /Political Leadership -->

  <div class="inf-footer">
    <strong>Common thread across all 18:</strong> deep observational patience · comfort with uncertainty · skepticism of surface appearances · systems thinking<br>
    <small>Photos via <a href="https://commons.wikimedia.org" target="_blank">Wikimedia Commons</a> — click any portrait for full attribution · All images Creative Commons licensed</small>
  </div>

</div><!-- /infographic-wrap -->
