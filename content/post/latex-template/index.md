---
title: "LaTeX Template for Research Papers"
subtitle: 
date: "2025-10-15"
summary: >
  This is a RevTeX template for research papers with appendix-only table of contents and correct bookmarks.
draft: false
featured: true
categories: ["Tech"]
---

Below is a copy‑pasteable LaTeX template (RevTeX 4.2) with an appendix‑only table of contents and correct PDF bookmarks.
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

% ignore \label warning
\usepackage{silence}
\WarningFilter{nameref}{The definition of \label has changed}

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
  bookmarks=true,
  colorlinks=true,
  urlcolor=webbrown,
  linkcolor=blueviolet, 
  citecolor=webgreen,
  pdfstartpage=1,
  pdfstartview={FitH},  % FitBH
  bookmarksopen=false
  ]{hyperref}
\usepackage{cleveref}

% --- 1) Mark the start of appendices *in the .toc* ---
\makeatletter
\pretocmd{\appendix}{\addtocontents{toc}{\protect\appsectionstart}}{}{}
\makeatother

% --- 2) A TOC printer that shows entries only *after* that marker ---
\makeatletter
\newcommand{\appendixtableofcontents}{%
  \begingroup
    \newif\ifapptoc \apptocfalse
    \let\rev@l@section\l@section
    \let\rev@l@subsection\l@subsection
    \let\rev@l@subsubsection\l@subsubsection
    \def\appsectionstart{\global\apptoctrue}
    \def\l@section##1##2{\ifapptoc\rev@l@section{##1}{##2}\fi}
    \def\l@subsection##1##2{\ifapptoc\rev@l@subsection{##1}{##2}\fi}
    \def\l@subsubsection##1##2{\ifapptoc\rev@l@subsubsection{##1}{##2}\fi}

    \setcounter{tocdepth}{2}%
    \phantomsection
    {%
      % swallow any \addcontentsline from the heading itself
      \let\addcontentsline\@gobblethree
      \section*{Contents}%
    }%
    \pdfbookmark[1]{Supplementary Information Contents}{apxcontents}

    \@starttoc{toc}%
  \endgroup
}
\makeatother

\newtheorem{theorem}{Theorem}
\newtheorem{lemma}{Lemma}
\newtheorem{corollary}{Corollary}
\newtheorem{definition}{Definition}
\newtheorem{remark}{Remark}

\bibliographystyle{apsrev4-2}

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
\renewcommand*\appendixpagename{Supplementary Information}
\appendix
\appendixpage
\appendixtableofcontents

\section{Appendixes}

\end{document}
%
% ****** End of file apssamp.tex ******
```
