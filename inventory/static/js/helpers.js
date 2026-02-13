(() => {
  const qs = (selector, scope = document) => scope.querySelector(selector);
  const qsa = (selector, scope = document) => Array.from(scope.querySelectorAll(selector));

  const on = (element, eventName, handler, options) => {
    if (!element) return () => {};
    element.addEventListener(eventName, handler, options);
    return () => element.removeEventListener(eventName, handler, options);
  };

  const debounce = (fn, wait = 200) => {
    let timeoutId;
    return (...args) => {
      window.clearTimeout(timeoutId);
      timeoutId = window.setTimeout(() => fn(...args), wait);
    };
  };

  const throttle = (fn, wait = 200) => {
    let lastRun = 0;
    let timeoutId;
    return (...args) => {
      const now = Date.now();
      const remaining = wait - (now - lastRun);
      if (remaining <= 0) {
        lastRun = now;
        fn(...args);
      } else {
        window.clearTimeout(timeoutId);
        timeoutId = window.setTimeout(() => {
          lastRun = Date.now();
          fn(...args);
        }, remaining);
      }
    };
  };

  const toggleClass = (element, className, force) => {
    if (!element) return;
    if (typeof force === "boolean") {
      element.classList.toggle(className, force);
    } else {
      element.classList.toggle(className);
    }
  };

  const getCookie = (name) => {
    const match = document.cookie.match(new RegExp(`(^| )${name}=([^;]+)`));
    return match ? decodeURIComponent(match[2]) : null;
  };

  window.Helpers = {
    qs,
    qsa,
    on,
    debounce,
    throttle,
    toggleClass,
    getCookie,
  };
})();
