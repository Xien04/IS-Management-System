(() => {
  const { qsa, on, debounce } = window.Helpers || {};

  const initAutoDismissMessages = () => {
    qsa?.(".message").forEach((msg) => {
      const remove = () => msg.classList.add("fade-out");
      const timeoutId = window.setTimeout(remove, 4500);
      on?.(msg, "click", () => {
        window.clearTimeout(timeoutId);
        remove();
      });
      on?.(msg, "transitionend", () => msg.remove());
    });
  };

  const initTableHover = () => {
    qsa?.(".table tr").forEach((row) => {
      on?.(row, "mouseenter", () => row.classList.add("row-hover"));
      on?.(row, "mouseleave", () => row.classList.remove("row-hover"));
    });
  };

  const initResponsiveNav = () => {
    const nav = document.querySelector("nav");
    if (!nav) return;
    let lastScroll = 0;
    const handler = () => {
      const current = window.scrollY || 0;
      if (current > lastScroll + 10) {
        nav.classList.add("nav-hidden");
      } else if (current < lastScroll - 10) {
        nav.classList.remove("nav-hidden");
      }
      lastScroll = current;
    };
    window.addEventListener("scroll", debounce?.(handler, 100) || handler);
  };

  document.addEventListener("DOMContentLoaded", () => {
    initAutoDismissMessages();
    initTableHover();
    initResponsiveNav();
  });
})();
