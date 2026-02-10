---
title: "LaTeX Template for Research Papers"
subtitle: 
date: "2025-10-15"
summary: >
  This is a RevTeX template for reader-friendly long appendices.
draft: false
featured: true
categories: ["Tech"]
---

Below is a copy‑pasteable LaTeX template (RevTeX 4.2) for reader-friendly long appendices.

It has an appendix‑only table of contents, correct PDF bookmarks, and clickable page numbers that will bring the readers back to the contents.

All warnings are fixed.

```latex
% ****** Start of file apssamp.tex ******
%
%   This file is part of the APS files in the REVTeX 4.2 distribution.
%   Version 4.2a of REVTeX, December 2014
%
%   Copyright (c) 2014 The American Physical Society.
%
%   See the REVTeX 4 README file for restrictions and more information.
%
% TeX'ing this file requires that you have AMS-LaTeX 2.0 installed
% as well as the rest of the prerequisites for REVTeX 4.2
%
% See the REVTeX 4 README file
% It also requires running BibTeX. The commands are as follows:
%
%  1)  latex apssamp.tex
%  2)  bibtex apssamp
%  3)  latex apssamp.tex
%  4)  latex apssamp.tex
%
\documentclass[%
%reprint,
%superscriptaddress,
%groupedaddress,
%unsortedaddress,
%runinaddress,
%frontmatterverbose, 
%preprint,
%preprintnumbers,
%nofootinbib,
%nobibnotes,
%bibnotes,
 amsmath,amssymb,
 aps,
 pra,
%prb,
%rmp,
%prstab,
%prstper,
%floatfix,
10pt,
]{revtex4-2}

\usepackage{silence}
\WarningFilter{nameref}{The definition of \label has changed}

\usepackage{fancyhdr}
\setlength{\headheight}{15pt} % prevent headheight warnings/loops

% Define your fancy style once
\fancypagestyle{header}{
  \fancyhf{}%
  \fancyhead[R]{\hyperref[toc]{\thepage}}%
  \renewcommand{\headrulewidth}{0pt}%
}

\usepackage{cmap} % Load before fontenc 
\usepackage[utf8]{inputenc}
\usepackage[english]{babel}
\usepackage[T1]{fontenc}
\usepackage{appendix}
\usepackage{url, dsfont, tikz, listings, xcolor, graphicx}
\usepackage[shortlabels]{enumitem}
\usepackage{amsfonts, amsmath, amssymb, amstext, amscd, amsthm, makeidx, mathrsfs, mathtools, longdivision, polynom, bbm, complexity, nicefrac, booktabs, physics, braket}
\usepackage[linesnumbered,ruled,vlined]{algorithm2e}
\usepackage[normalem]{ulem}

\definecolor{blueviolet}{rgb}{0.2, 0.2, 0.6}
\definecolor{webgreen}{rgb}{0,.5,0}
\definecolor{webbrown}{rgb}{.6,0,0}
\usepackage[pdftex,
  bookmarks=false,
  colorlinks=true,
  urlcolor=webbrown,
  linkcolor=blueviolet, 
  citecolor=webgreen,
  pdfstartpage=1,
  pdfstartview={FitH},  % FitBH
  bookmarksopen=false
  ]{hyperref}
\usepackage{cleveref}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{task}[theorem]{Task}

\renewcommand{\E}{\mathbb{E}}
\newcommand{\Var}{\mathrm{Var}}
\newcommand{\Cov}{\mathrm{Cov}}
\newcommand{\bit}{\{0, 1\}}
\newcommand{\unif}{\mathrm{Uniform}}
\newcommand{\floor}[1]{\left\lfloor#1\right\rfloor}
\newcommand{\ceil}[1]{\left\lceil#1\right\rceil}
\newcommand{\dtv}{d_{\mathrm{TV}}}
\newcommand{\argmax}{\mathrm{argmax}}
\newcommand{\diag}{\mathrm{diag}}
\newcommand{\sgn}{\mathrm{sgn}}
\newcommand{\lr}[1]{\left(#1\right)}
\newcommand{\cD}{\mathcal{D}}
\newcommand{\cE}{\mathcal{E}}
\newcommand{\cN}{\mathcal{N}}
\newcommand{\cO}{\mathcal{O}}
\newcommand{\cU}{\mathcal{U}}
\newcommand{\cV}{\mathcal{V}}

\NewDocumentEnvironment{eqsplit}{b}{%
    \begin{equation}%
    \begin{split}%
        #1
    \end{split}%
    \end{equation}%
}{}

\makeatletter

% 1. Define the appendix-only TOC file extension
\newcommand{\apptocfile}{atoc}

% 2. Hook \appendix
\let\apptoc@orig@appendix\appendix
\renewcommand{\appendix}{%
  % Call the original appendix command to handle counters/formatting
  \apptoc@orig@appendix
  % Redefine \addtocontents instead of \addcontentsline.
  % This allows hyperref to see 'toc' (triggering the bookmark write)
  % but intercepts the actual file write to redirect it to .atoc.
  \let\apptoc@orig@addtocontents\addtocontents
  \long\def\addtocontents##1##2{%
    \def\apptoc@ext{##1}%
    \def\apptoc@toc{toc}%
    \ifx\apptoc@ext\apptoc@toc
      \apptoc@orig@addtocontents{\apptocfile}{##2}%
    \else
      \apptoc@orig@addtocontents{##1}{##2}%
    \fi
  }%
}

% 3. Print appendix-only TOC
\newcommand{\appendixtableofcontents}{%
  \begingroup
    \setcounter{tocdepth}{3}%
    \phantomsection
    % Swallow any \addcontentsline from the heading itself to prevent
    % the "Contents" header from appearing in the TOC recursively.
    \let\addcontentsline\@gobblethree
    \section*{Contents \& Roadmap}%
    % Add a bookmark for the Appendix TOC itself
    \pdfbookmark[1]{Appendices}{apxcontents}%
    % Read the .atoc file
    \@starttoc{\apptocfile}%
  \endgroup
}

\makeatother

\bibliographystyle{unsrt}

\begin{document}

\title{Title}

\author{Author}
\email{email@email.com}
\affiliation{Affiliation}

\begin{abstract}
Abstract
\end{abstract}

\maketitle

\section{Introduction}
Introduction \cite{nielsen2010quantum}.

\section*{Acknowledgments}
Acknowledgments.

\bibliography{ref}

\clearpage
\onecolumngrid
\renewcommand*\appendixpagename{Appendices}
\appendix
\appendixpage

\pagestyle{header}

\appendixtableofcontents
\label{toc}

\section{Appendixes}

\end{document}
%
% ****** End of file apssamp.tex ******
```
