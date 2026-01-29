import { useEffect } from 'react';

export function useResizeObserver(ref, onResize) {
  useEffect(() => {
    if (!ref.current) return;
    const el = ref.current;
    const ro = new ResizeObserver(entries => {
      for (const entry of entries) onResize(entry.contentRect);
    });
    ro.observe(el);
    return () => ro.disconnect();
  }, [ref, onResize]);
}
