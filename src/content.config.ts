import { z, defineCollection } from "astro:content";
import { glob } from "astro/loaders";

export type BlogSchema = z.infer<ReturnType<typeof createBlogSchema>>;

const createBlogSchema = ({ image }: { image: any }) => z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    heroImage: image().optional(),
    badge: z.string().optional(),
    tags: z.array(z.string()).refine(items => new Set(items).size === items.length, {
        message: 'tags must be unique',
    }).optional(),
});

const blogCollection = defineCollection({
    loader: glob({ pattern: "**/*.{md,mdx}", base: "./src/content/blog" }),
    schema: createBlogSchema,
});

export const collections = {
    'blog': blogCollection,
}
