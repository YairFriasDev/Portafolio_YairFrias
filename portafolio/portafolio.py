# portafolio/portafolio.py

import reflex as rx
from portafolio import data
from portafolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portafolio.views.about import about
from portafolio.views.extra import extra
from portafolio.views.footer import footer
from portafolio.views.header import header
from portafolio.views.info import info
from portafolio.views.tech_stack import tech_stack

DATA = data.data

# -------------------------------------------------------------
# CSS inline para tipado, halo, reveal, hover-zoom y botones
# -------------------------------------------------------------
INLINE_CSS = """
<style>
  .typing-effect {
    display: inline-block;
    border-right: 2px solid currentColor;
    white-space: nowrap;
    overflow: hidden;
    animation: blink 0.75s step-end infinite;
  }
  @keyframes blink {
    0%, 100% { border-color: transparent; }
    50% { border-color: currentColor; }
  }

  .halo-effect {  
    border-radius: 9999px;
    animation: glow 2s ease-in-out infinite alternate;
  }

  @keyframes glow {
  0%, 100% { filter: drop-shadow(0 0 8px #FFD700); }
  50%      { filter: drop-shadow(0 0 32px #FFD700); }
}

  @keyframes pulse {
    0% {
      filter: drop-shadow(0 0 4px #FFD700);
    }
    50% {
      filter: drop-shadow(0 0 16px #FFD700);
    }
    100% {
      filter: drop-shadow(0 0 4px #FFD700);
    }
  }

  .reveal {
    opacity: 0;
    transform: translateX(-20px);
    transition: opacity 0.7s ease-out, transform 0.7s ease-out;
  }
  .reveal.visible {
    opacity: 1;
    transform: translateX(0);
  }

  .hover-zoom { transition: transform 0.3s ease-in-out; }
  .hover-zoom:hover { transform: scale(1.05); }

  .circle-button {
    width: 2.5rem;
    height: 2.5rem;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border: 1px solid currentColor;
    border-radius: 9999px;
    transition: border-color 0.2s;
  }
  .circle-button:hover { border-color: #ccc; }
</style>
"""

# -------------------------------------------------------------
# JS inline: inicializa tema, typing-effect adaptado y define toggleTheme()
# -------------------------------------------------------------
INLINE_JS = """
(function() {
  // Inicializa tema light/dark
  const t = localStorage.getItem('theme') || 'light';
  document.documentElement.classList.toggle('dark', t === 'dark');

  // Efecto máquina de escribir infinito, conservando la primera letra
  const el = document.querySelector('.typing-effect');
  if (el) {
    const fullText = el.textContent;
    let index = 0;
    let isDeleting = false;
    const minIndex = 1; // Mantener la primera letra
    setInterval(() => {
      el.textContent = fullText.substring(0, index);
      if (!isDeleting) {
        if (index < fullText.length) {
          index++;
        } else {
          isDeleting = true;
        }
      } else {
        if (index > minIndex) {
          index--;
        } else {
          isDeleting = false;
        }
      }
    }, 150);
  }
})();

// Función para alternar tema
function toggleTheme() {
  const isDark = document.documentElement.classList.toggle('dark');
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
}
"""


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            # Inyecta CSS y JS inline
            rx.html("", dangerouslySetInnerHTML={"__html": INLINE_CSS}),
            rx.script(INLINE_JS),

            # Tu layout
            header(DATA),
            about(DATA.about),
            rx.divider(),
            tech_stack(DATA.technologies),
            info("Experience", DATA.experience),
            info("Projects", DATA.projects),
            info("Education & Training", DATA.training),
            extra(DATA.extras),
            rx.divider(),
            footer(DATA.media),

            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%"
        )
    )

app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(
        appearance="dark",
        accent_color="grass",
        radius="full"
    )
)

app.add_page(
    index,
    title=DATA.title,
    description=DATA.description,
    image=DATA.image,
    meta=[
        {"name": "og:title", "content": DATA.title},
        {"name": "og:description", "content": DATA.description},
        {"name": "og:image", "content": DATA.image},
    ],
)

if __name__ == "__main__":
    app.run()