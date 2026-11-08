import type { Metadata } from "next";
import { Nunito } from "next/font/google";
import "./globals.css";

const nunito = Nunito({
  subsets: ["latin", "latin-ext"],
  weight: ["400", "500", "600", "700", "800"],
  display: "swap",
  variable: "--font-nunito",
});

export const metadata: Metadata = {
  title: "Magistr Seçim | Uyğun ixtisasını tap",
  description:
    "Bakalavr ixtisasına uyğun magistr proqramlarını və universitetləri tap.",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="az" className={nunito.className}>
      <body>{children}</body>
    </html>
  );
}
