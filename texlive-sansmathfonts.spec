%global tl_name sansmathfonts
%global tl_revision 77723

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Extended Computer Modern sans serif fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/sansmathfonts
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sansmathfonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sansmathfonts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Sans serif small caps and math fonts for use with Computer Modern.

