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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Sans serif small caps and math fonts for use with Computer Modern.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from sansmathfonts:
Map sansmathfonts.map
TL_DROPIN_EOF
