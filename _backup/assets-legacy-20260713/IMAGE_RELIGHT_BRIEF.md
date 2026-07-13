# NINE ONE Image Relight Brief

This is the required workflow for the next image pass. Do not use a flat color grade, overlay, LUT, CSS filter, or global mask as the final output.

## Goal

Use true image-to-image editing on each source image.

Same scene, same composition, same architecture, same camera angle. Preserve all structural elements precisely. Re-render the lighting and atmosphere only.

## Source

Use the originals in:

`nine-one-website/assets/images/`

Do not use `images-brand-v2` or any previous filtered output as the source.

## Output

Write finished files to a new folder:

`nine-one-website/assets/images-img2img-golden-hour/`

Keep every filename and original aspect ratio unchanged.

## Positive Prompt

Same scene, same composition, same architecture, same camera angle, preserve all structural elements precisely. Re-render the lighting and atmosphere as bright dusk architectural photography, golden hour or early morning soft daylight, warm color temperature 3500K, soft white #F5F5F3 dominant, warm shadows, no cold cyan, natural sunlight on architecture, calm premium atmosphere, editorial photography style inspired by Reserve Padel, Aman, Soho House, and Aesop, spacious breathable architectural composition, desaturated by 20 percent from commercial photography, lifted shadows, retained midtone detail, no crushed blacks, realistic materials, subtle warm highlights, high-end sports infrastructure photography.

## Negative Prompt

Do not change architecture, structure, camera angle, layout, logo placement, people count, court lines, fences, buildings, furniture, product shape, or composition. No neon glow, no cyberpunk lighting, no studio strobe, no HDR pop, no overlay graphics, no connection lines, no extra text, no new logos, no fantasy elements, no cold cyan shadows, no crushed blacks, no excessive contrast, no oversaturated green or blue, no plastic CGI look.

## Settings

- Strength / denoise: `0.45-0.55`
- Aspect ratio: keep original
- Resize: no crop
- Control guidance if available: use structure/depth/edge control at medium-high strength
- Seed: fixed per image after first acceptable result
- Output format: same extension unless the tool requires PNG/JPG

## Acceptance Criteria

- The result looks relit, not color-filtered.
- Shadows are visibly lifted but still dimensional.
- Sunlight and warmth interact with architecture and scene surfaces.
- No cold cyan cast remains in shadow areas.
- Structural details match the original image.
- No added graphic overlays, light trails, connection arcs, or UI lines.
- The page should not reference this folder until the visual pass is approved.
