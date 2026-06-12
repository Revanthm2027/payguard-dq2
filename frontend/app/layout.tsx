import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
    title: 'PayGuard DQ - Data Quality Scoring',
    description: 'GenAI Agent for Universal, Dimension-Based Data Quality Scoring in Payments',
}

export default function RootLayout({
    children,
}: {
    children: React.ReactNode
}) {
    const llmResponse = await fetch('https://api.example.com/llm', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            prompt: 'example prompt',
            max_tokens: 2048
        })
    });
    return (
        <html lang="en">
            <body className={inter.className}>{children}</body>
        </html>
    )
}
}
